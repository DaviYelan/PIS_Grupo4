from controllers.dao.daoAdapter import DaoAdapter
from models.estudiante import Estudiante, load_data, save_data, calculate_averages
from flask import ( Blueprint,jsonify,render_template, request, redirect,url_for,flash,current_app,)
from werkzeug.utils import secure_filename
import io
import os
import smtplib
import base64
import pandas as pd #type: ignore
import matplotlib #type: ignore
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt #type: ignore

matplotlib.use("Agg")

student_blueprint = Blueprint("students", __name__)


class EstudianteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estudiante)
        self.__estudiante = None

    @property
    def estudiante(self):
        if self.__estudiante is None:
            self.__estudiante = Estudiante()
        return self.__estudiante

    @estudiante.setter
    def estudiante(self, value):
        self.__estudiante = value

    def save(self):
        data = load_data()
        new_id = max(data.keys()) + 1 if data else 1
        self.estudiante._id = new_id
        data[new_id] = self.estudiante.serializable
        save_data(data)

    def merge(self, id):
        data = load_data()
        if id in data:
            data[id] = self.estudiante.serializable
            save_data(data)

    def delete(self, id):
        data = load_data()
        if id in data:
            del data[id]
            save_data(data)


def generate_chart(results):
    students = [result[0] for result in results]
    averages = [result[1] for result in results]

    plt.figure(figsize=(10, 6))
    plt.bar(students, averages, color="skyblue")
    plt.xlabel("Estudiantes")
    plt.ylabel("Promedio")
    plt.title("Promedio de Calificaciones por Estudiante")
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    chart = base64.b64encode(img.getvalue()).decode("utf8")

    plt.close()
    return chart


def filter_students(data, category):
    if category == "A":
        return {k: v for k, v in data.items() if v["categoria"] == "A"}
    elif category == "B":
        return {k: v for k, v in data.items() if v["categoria"] == "B"}
    elif category == "C":
        return {k: v for k, v in data.items() if v["categoria"] == "C"}
    elif category == "D":
        return {k: v for k, v in data.items() if v["categoria"] == "D"}
    return data


@student_blueprint.route("/")
def index():
    data = load_data()
    results = calculate_averages(data)
    chart = generate_chart(results)
    return render_template("index.html", results=results, chart=chart)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"xls", "xlsx"}


def process_excel(filepath, unit):
    data = pd.read_excel(filepath)
    student_data = load_data()

    for index, row in data.iterrows():
        student = f"{row['Nombre']} {row['Apellido']}"
        scores = [row[f"Nota{i}"] for i in range(1, 4) if f"Nota{i}" in row]
        matricula = row["Matricula"]
        if student in student_data:
            student_data[student][unit] = scores
        else:
            student_data[student] = {unit: scores, "matricula": matricula}

    save_data(student_data)


def generate_chart(results):
    students = list(results.keys())
    averages = [result["average"] for result in results.values()]

    plt.figure(figsize=(10, 6))
    plt.bar(students, averages)
    plt.xlabel("Estudiantes")
    plt.ylabel("Promedio")
    plt.title("Promedio de Calificaciones por Estudiante")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    chart = base64.b64encode(img.getvalue()).decode()

    plt.close()
    return chart


@student_blueprint.route(
    "/login/moduloDocentes/delete_student/<student>", methods=["POST"]
)
def delete_student(student):
    data = load_data()
    if student in data:
        del data[student]
        save_data(data)
        flash(f"{student} ha sido eliminado con éxito")
    else:
        flash(f"{student} no fue encontrado")
    return redirect(url_for("students.index"))


@student_blueprint.route(
    "/login/moduloDocentes/update_student/<matricula>", methods=["POST"]
)
def update_student(matricula):
    data = load_data()
    student = next((s for s in data if data[s]["matricula"] == matricula), None)
    if student:
        data[student]["scores"] = request.json["scores"]
        save_data(data)
        return jsonify(
            {
                "status": "success",
                "message": f"Estudiante con matrícula {matricula} actualizado.",
            }
        )
    return jsonify({"status": "error", "message": "Estudiante no encontrado."}), 404


@student_blueprint.route("/send_excel_to_admin")
def send_excel_to_admin():
    data = load_data()
    results = calculate_averages(data)
    df = pd.DataFrame(results).T
    excel_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"], "students_report.xlsx"
    )
    df.to_excel(excel_path, index=True)

    sender_email = "Correo del que envia"
    receiver_email = "Correo del que recive"
    password = "Contraseña de programa de correo"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Students Report Excel"

    part = MIMEBase("application", "octet-stream")
    with open(excel_path, "rb") as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(excel_path)}",
    )
    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)

    flash("Excel sent to admin successfully")
    return redirect(url_for("students.index"))


@student_blueprint.route("/login/moduloDocentes/upload", methods=["POST"])
def upload_file():
    files = [request.files.get(f"file{i}") for i in range(1, 4)]

    if not all(files):
        flash("All three files are required")
        return redirect(url_for("students.index"))

    for i, file in enumerate(files, start=1):
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            process_excel(filepath, f"unit{i}")

    flash("Files successfully uploaded")
    return redirect(url_for("students.index"))


# @student_blueprint.route("/calculate", methods=["POST"])
# def calculate():
#     student = request.form["student"]
#     scores = request.form["score"].split(",")
#     matricula = int(request.form["matricula"])
#     data = load_data()

#     if student in data:
#         data[student]["scores"].extend(scores)
#     else:
#         data[student] = {"scores": scores, "matricula": matricula}

#     save_data(data)

#     results = calculate_averages(data)
#     chart = generate_chart(results)

#     return render_template("index.html", results=results, chart=chart)


# @student_blueprint.route("/filter", methods=["GET", "POST"])
# def filter_students_view():
#     if request.method == "POST":
#         category = request.form["category"]
#         data = load_data()
#         results = calculate_averages(data)
#         filtered_results = filter_students(results, category)
#         chart = generate_chart(filtered_results)
#         return render_template(
#             "filter.html", results=filtered_results, chart=chart, category=category
#         )
#     return render_template("index.html")


# @student_blueprint.route("/download/<category>")
# def download_filtered(category):
#     data = load_data()
#     results = calculate_averages(data)
#     filtered_results = filter_students(results, category)
#     df = pd.DataFrame(filtered_results).T

#     excel_path = os.path.join(
#         current_app.config["UPLOAD_FOLDER"], f"filtered_students_{category}.xlsx"
#     )
#     df.to_excel(excel_path, index=True)

#     return send_file(excel_path, as_attachment=True)


# @student_blueprint.route("/download_pdf/<category>")
# def download_filtered_pdf(category):
#     data = load_data()
#     results = calculate_averages(data)
#     filtered_results = filter_students(results, category)

#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(200, 10, f"Alumnos en la categoría {category}", ln=True, align="C")
#     pdf.ln(10)
#     pdf.set_font("Arial", "", 12)

#     for student, info in filtered_results.items():
#         pdf.cell(200, 10, f"{student}: {info['average']}", ln=True)

#     pdf_path = os.path.join(
#         current_app.config["UPLOAD_FOLDER"], f"filtered_students_{category}.pdf"
#     )
#     pdf.output(pdf_path)

#     return send_file(pdf_path, as_attachment=True)


# @student_blueprint.route("/login/moduloDocentes/filter")
# def filter_students():
#     filter_type = request.args.get("type")
#     filter_value = request.args.get("value")
#     matricula = request.args.get("matricula")

#     data = load_data()
#     results = calculate_averages(data)

#     if filter_type == "promedio":
#         filtered_results = {k: v for k, v in results.items() if v["categoria"] == filter_value}
#     else:
#         filtered_results = {k: v for k, v in results.items() if v["matricula"] == matricula}

#     return jsonify(filtered_results)


# @student_blueprint.route("/login/moduloDocentes/download_excel")
# def download_excel():
#     data = load_data()
#     results = calculate_averages(data)
#     df = pd.DataFrame(results).T
#     excel_path = os.path.join(
#         current_app.config["UPLOAD_FOLDER"], "students_report.xlsx"
#     )
#     df.to_excel(excel_path, index=True)
#     return send_file(excel_path, as_attachment=True)


# @student_blueprint.route("/login/moduloDocentes/generate_report")
# def generate_report():
#     data = load_data()
#     results = calculate_averages(data)

#     df = pd.DataFrame.from_dict(results, orient="index")
#     df["promedio_unidades"] = df["unit_scores"].apply(
#         lambda x: sum(sum(unit) for unit in x.values())
#         / sum(len(unit) for unit in x.values())
#     )

#     excel_path = os.path.join(
#         current_app.config["UPLOAD_FOLDER"], "student_report.xlsx"
#     )
#     df.to_excel(excel_path, index=True)

#     return send_file(
#         excel_path, as_attachment=True, attachment_filename="student_report.xlsx"
#     )
