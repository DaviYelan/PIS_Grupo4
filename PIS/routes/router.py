from datetime import datetime
from controllers.cursaDaoControl import CursaDaoControl
from models.cursa import Cursa
from models.docente import Docente
from models.materia import Materia
from models.estudiante import calculate_averages, load_data, load_excel_data, save_data
from controllers.estudianteDaoControl import (EstudianteDaoControl,filter_students,generate_chart,)
from flask import Blueprint, app, current_app, g, jsonify, render_template, redirect, request, flash, abort, send_file, session, url_for
from controllers.asignacionDaoControl import AsignacionDaoControl
from controllers.connecction.connection import Connection
from controllers.personaDaoControl import PersonaDaoControl
from flask_login import logout_user, login_required, login_user, LoginManager # type: ignore
from models.Modelcuenta import ModelCuenta
from models.cuenta import Cuenta
from controllers.docenteDaoControl import DocenteDaoControl
from controllers.materiaDaoControl import MateriaDaoControl
from werkzeug.utils import secure_filename
from fpdf import FPDF # type: ignore
import pandas as pd # type: ignore
import json
import os



router = Blueprint('router', __name__)

@router.route('/')
def home():
    return redirect("/login")

@router.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cuenta = Cuenta(0, username, password)
        logged_user = ModelCuenta.login(g.db, cuenta)
        if logged_user:
            if logged_user.clave:
                login_user(logged_user)
                if logged_user.rol == 'admin':
                    return redirect("/login/moduloAdmin")
                elif logged_user.rol == 'docente':
                    return redirect("/login/moduloDocentes")
                elif logged_user.rol == 'encargado':
                    return redirect("/login/moduloEncargado")
                else:
                    flash("Rol no encontrado")
            else:
                flash("Usuario no encontrado")
        else:
            flash("Usuario o contraseña incorrectos")
    return render_template("tempsLogin/auth/login.html")

@router.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


#---------------MODULO DE ADMIN-----------------
@router.route("/login/moduloEncargado")
def moduloEncargado():
    return render_template("tempsFranco/index.html")

@router.route('/login/moduloAdmin')
def moduloAdmin():
    return render_template('tempsAdmin/docente/accion.html')

@router.route("/sala")
# @login_required
def sala():
    return render_template("tempsMensajes/sala.html")


# ------------------------Sección de asignaciones----------------------------------------------------------------
@router.route('/asignarMaestro', methods=['GET', 'POST'])
def asignarMaestro():
    if request.method == 'POST':
        docente_id = request.form.get('docente')
        materia_id = request.form.get('materia')
        print(f"Docente ID: {docente_id}, Materia ID: {materia_id}")
        if not docente_id or not materia_id :
            print("Error: Docente ID o Materia ID está vacío.")
            return redirect('/asignarMaestro', code=302)
        connection = Connection()
        connection.connect()
        asignacion_control = AsignacionDaoControl(connection)
        try:
            asignacion_control.save_asignacion(docente_id, materia_id)
        except Exception as e:
            print(f"Error al guardar asignación: {e}")
        finally:
            connection.close()
        return redirect('/asignarMaestro', code=302)
    connection = Connection()
    connection.connect()
    docente_control = DocenteDaoControl(connection)
    docentes = docente_control._lista
    materia_control = MateriaDaoControl(connection)
    materias = materia_control._lista
    query = """
        SELECT 
            a.ID AS ASIGNACION_ID, 
            d.nombre AS DOCENTE_NOMBRE, 
            m.nombre AS MATERIA_NOMBRE,
            m.ciclo AS CICLO_NOMBRE
        FROM 
            ASIGNACION a
        JOIN 
            DOCENTE d ON a.DOCENTE_ID = d.ID
        JOIN 
            MATERIA m ON a.MATERIA_ID = m.ID
    """
    try:
        cursor = connection.execute(query)
        asignaciones = cursor.fetchall()
        print(f"Asignaciones recuperadas: {asignaciones}")
    except Exception as e:
        print(f"Error al recuperar asignaciones: {e}")
        asignaciones = []
    connection.close()
    return render_template('tempsAdmin/gestion/asignacion.html', docentes=docentes, materias=materias, asignaciones=asignaciones, cursos=cursos)
#------------------------Sección de Cursos----------------------------------------------------------------
#acciones de cursos
@router.route('/cursos')
def cursos():
    connection = Connection()
    connection.connect()
    cursa_control = CursaDaoControl(connection)
    cursos = cursa_control._lista
    connection.close()
    return render_template('tempsAdmin/gestion/cursos.html', cursos=cursos)

#------------------------Sección de Docentes----------------------------------------------------------------
#acciones de docente
@router.route('/accionDocente')
def ver_opcionesDocentes():
    return render_template('tempsAdmin/docente/accion.html')

@router.route('/registrarDocentes')
def ver_guardar():
    return render_template('tempsAdmin/docente/registrar.html')

#LISTA DE DOCENTES
@router.route('/listaDocentes')
def ver_docentes():
    connection = Connection()
    connection.connect()
    docente_control = DocenteDaoControl(connection)
    docentes = docente_control._lista 
    connection.close()
    print(f"Docentes List: {docentes}")  
    return render_template('tempsAdmin/docente/lista.html', lista=docentes)

#MOSTRAR LISTA DE DOCENTES
@router.route('/docentes/ver')
def ver():
    return render_template('tempsAdmin/docente/registrar.html')

#guardar docentes
@router.route('/registrarDocentes/guardar', methods=['POST'])
def guardar_docentes():
    connection = Connection()
    connection.connect()
    dc = DocenteDaoControl(connection)
    nuevo_docente = Docente()
    nuevo_docente._nombre = request.form.get('nombre')
    nuevo_docente._apellido = request.form.get('apellido')
    fecha_str = request.form.get('fecha')
    try:
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Obtener solo la parte de la fecha
        nuevo_docente._fecha = fecha_obj
    except ValueError:
        print("Error: La fecha debe estar en formato YYYY-MM-DD")
        return redirect('/registrarDocentes', code=302)  # Redirigir en caso de error en el formato de la fecha
    nuevo_docente._telefono = request.form.get('telefono')
    nuevo_docente._correo = request.form.get('correo')
    nuevo_docente._genero = request.form.get('genero')
    nuevo_docente._tipoIdentificacion = request.form.get('tipoIdentificacion')
    nuevo_docente._tituloCuartoNivel = request.form.get('tituloCuartoNivel')
    nuevo_docente._especialidad = request.form.get('especialidad')
    nuevo_docente._cubiculo = request.form.get('cubiculo')
    dc._docente = nuevo_docente
    dc.save  
    connection.close()

    return redirect('/listaDocentes', code=302)

#editar docentes
@router.route('/registrarDocentes/editar/<int:id>', methods=['GET'])
def editar(id):
    connection = Connection()
    connection.connect()
    dc = DocenteDaoControl(connection)
    docente = dc._get(id)
    if not docente:
        connection.close()
        return redirect('/listaDocentes', code=302)
    connection.close()
    return render_template('tempsAdmin/docente/editar.html', docente=docente)

#modificar docentes
@router.route('/registrarDocentes/modificar', methods=['POST'])
def modificar():
    connection = Connection()
    connection.connect()
    dc = DocenteDaoControl(connection)
    data = request.form
    pos = int(data["id"]) 
    
    docente = dc._get(pos)
    if not docente:
        print(f"Error: No se encontró el docente con ID {pos}")
        connection.close()
        return redirect('/listaDocentes', code=302)
    
    docente._nombre = request.form.get('nombre')
    docente._apellido = request.form.get('apellido')
    fecha_str = request.form.get('fecha')
    try:
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        docente._fecha = fecha_obj
    except ValueError:
        print("Error: La fecha debe estar en formato YYYY-MM-DD")
        connection.close()
        return redirect('/listaDocentes', code=302)
    
    docente._telefono = request.form.get('telefono')
    docente._correo = request.form.get('correo')
    docente._genero = request.form.get('genero')
    docente._tipoIdentificacion = request.form.get('tipoIdentificacion')
    docente._tituloCuartoNivel = request.form.get('tituloCuartoNivel')
    docente._especialidad = request.form.get('especialidad')
    docente._cubiculo = request.form.get('cubiculo')
    dc._docente = docente
    dc.merge(pos)
    connection.close()
    return redirect("/listaDocentes", code=302)


#eliminar docentes
@router.route('/registrarDocentes/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    connection = Connection()
    connection.connect()
    dc = DocenteDaoControl(connection)                  
    try:
        dc._delete(id)
        connection.connection.commit()
        response = {"success": True}
    except Exception as e:
        print(f"Error al eliminar el docente con ID {id}: {e}")
        connection.connection.rollback()
        response = {"success": False, "error": str(e)}
    finally:
        connection.close()
    
    return jsonify(response)


#----------------------------------SECCION MATERIA------------------------------------------------------

@router.route('/accionMateria')
def ver_opcionesMaterias():
    return render_template('tempsAdmin/materia/accionMateria.html')

#MOSTRAR LISTA DE MATERIAS
@router.route('/registrarMateria')
def ver_guardarMateria():
    return render_template('tempsAdmin/materia/registrarMateria.html')

#ver lista de materias
@router.route('/listaMateria')
def ver_materias():
    connection = Connection()
    connection.connect()
    materia = MateriaDaoControl(connection)
    materias = materia._lista
    connection.close()
    print(f"Materias List: {materias}")  
    return render_template('tempsAdmin/materia/lista.html', lista=materias)

#guardar materias
@router.route('/registrarMateria/guardar', methods=['POST'])
def guardar_materias():
    connection = Connection()
    connection.connect()
    mdc = MateriaDaoControl(connection)
    nueva_materia = Materia()
    nueva_materia._nombre = request.form.get('nombre')
    nueva_materia._codigo = request.form.get('codigo')
    nueva_materia._numeroHoraSemanal = int(request.form.get('horaSemanal', 0))
    nueva_materia._ciclo = int(request.form.get('ciclo', 0))
    if not nueva_materia._ciclo:
        connection.close()
        return "El campo ciclo es obligatorio", 400

    mdc._materia = nueva_materia
    mdc.save
    connection.close()
    return redirect('/listaMateria', code=302)


#editar materias
@router.route('/registrarMateria/editar/<int:id>', methods=['GET'])
def editar_materia(id):
    connection = Connection()
    connection.connect()
    mdc = MateriaDaoControl(connection)
    materia = mdc._get(id)
    connection.close()
    if not materia:
        return redirect('/listaMateria', code=302)
    return render_template('tempsAdmin/materia/editar.html', materia=materia)

#modificar materias
@router.route('/registrarMateria/modificar', methods=['POST'])
def modificar_materia():
    connection = Connection()
    connection.connect()
    mdc = MateriaDaoControl(connection)
    data = request.form
    pos = int(data["id"])
    materia = mdc._get(pos)
    
    if not materia:
        connection.close()
        return redirect('/listaMateria', code=302)
    
    materia._nombre = request.form.get('nombre')
    materia._codigo = request.form.get('codigo')
    try:
        materia._numeroHoraSemanal = int(request.form.get('numeroHoraSemanal', 0))
        materia._ciclo = int(request.form.get('ciclo', 0))
        if materia._ciclo == 0:
            raise ValueError("El campo ciclo es obligatorio")
    except ValueError as e:
        connection.close()
        return str(e), 400
    
    mdc._materia = materia
    mdc.merge(pos)  # Llama al método merge para actualizar
    connection.close()
    return redirect("/listaMateria", code=302)

#eliminar materias
@router.route('/registrarMateria/eliminar/<int:id>', methods=['POST'])
def eliminar_materia(id):
    connection = Connection()
    connection.connect()
    dc = MateriaDaoControl(connection)                  
    try:
        dc._delete(id)
        connection.connection.commit()
        response = {"success": True}
    except Exception as e:
        print(f"Error al eliminar la Materia con ID {id}: {e}")
        connection.connection.rollback()
        response = {"success": False, "error": str(e)}
    finally:
        connection.close()
    
    return jsonify(response)

#---------------MODULO DE DOCENTE-----------------

@router.route('/login/moduloDocentes')
def moduloDocente():
    return render_template('tempsDocente/index.html')

@router.route('/get_materias')
def get_materias():
    materia_dao = MateriaDaoControl()
    materias = materia_dao.get_all()
    return jsonify(materias)

@router.route('/login/moduloDocentes/estudiantes')
def prueba():
    return render_template('tempsDocente/index.html')

@router.route("/upload_excel", methods=["POST"])
def upload_excel():
    unit = request.form.get("unit")
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        df = pd.read_excel(file_path)
        data = df.to_dict("records")
        if "excel_data" not in session:
            session["excel_data"] = {}
        session["excel_data"][unit] = data

        return jsonify({"message": f"File uploaded successfully for Unit {unit}"}), 200
    return jsonify({"error": "File type not allowed"}), 400


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"xlsx", "xls"}


@router.route("/login/moduloDocentes/download_excel")
def download_excel():
    data = load_data()
    results = calculate_averages(data)

    excel_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"], "students_report.xlsx"
    )

    with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
        for unit in ["unit1", "unit2", "unit3"]:
            unit_data = {
                student: {
                    "Id": info["id"],
                    "Matrícula": info["matricula"],
                    "Nombre": student.split()[0],
                    "Apellido(s)": student.split()[1] if len(student.split()) > 1 else "",
                    "Promedio": (
                        info["unit_scores"][unit]["average"]
                        if unit in info["unit_scores"]
                        else 0
                    ),
                    "Categoría": (
                        info["unit_scores"][unit]["category"]
                        if unit in info["unit_scores"]
                        else ""
                    ),
                    "Comentario": (
                        info["unit_scores"][unit].get("comment", "")
                        if unit in info["unit_scores"]
                        else ""
                    ),
                }
                for student, info in results.items()
                if unit in info["unit_scores"]
            }
            df_unit = pd.DataFrame(unit_data).T
            df_unit.to_excel(writer, sheet_name=f"Unit {unit[-1]}")

        df_final = pd.DataFrame(
            {
                student: {
                    "Id": info["id"],
                    "Matrícula": info["matricula"],
                    "Nombre": student.split()[0],
                    "Apellido(s)": student.split()[1] if len(student.split()) > 1 else "",
                    "Promedio Unidad 1": info["unit_scores"]
                    .get("unit1", {})
                    .get("average", 0),
                    "Promedio Unidad 2": info["unit_scores"]
                    .get("unit2", {})
                    .get("average", 0),
                    "Promedio Unidad 3": info["unit_scores"]
                    .get("unit3", {})
                    .get("average", 0),
                    "Promedio Final": info["average"],
                    "Categoría": info["categoria"],
                }
                for student, info in results.items()
            }
        ).T
        df_final.to_excel(writer, sheet_name="Final Averages")

    return send_file(excel_path, as_attachment=True)


@router.route("/login/moduloDocentes/download_all_units_excel")
def download_all_units_excel():
    data = load_data()
    results = calculate_averages(data)

    df = pd.DataFrame(results).T

    if "unit_scores" in df.columns:
        unit_scores_df = pd.json_normalize(df["unit_scores"])
        df = pd.concat([df.drop(columns=["unit_scores"]), unit_scores_df], axis=1)

    excel_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"], "all_units_report.xlsx"
    )
    df.to_excel(excel_path, index=True)

    return send_file(excel_path, as_attachment=True)


@router.route("/calculate", methods=["POST"])
def calculate():
    student = request.form["student"]
    scores = list(map(float, request.form["score"].split(",")))
    id = int(request.form["id"])
    matricula = int(request.form["matricula"])
    data = load_data()

    if student in data:
        data[student]["scores"].extend(scores)
    else:
        data[student] = {"id": id, "scores": scores, "matricula": matricula}

    save_data(data)

    results = calculate_averages(data)
    chart = generate_chart(results)

    return render_template("index.html", results=results, chart=chart)


@router.route("/calculate_final_averages")
def calculate_final_averages():
    data = load_data()
    results = calculate_averages(data)
    return jsonify(results)


@router.route("/login/moduloDocentes/filter")
def filter_students():
    category = request.args.get("category")
    matricula = request.args.get("matricula")

    filtered_results = {}
    for unit in ["unidad1", "unidad2", "unidad3"]:
        if unit in session.get("excel_data", {}):
            for student in session["excel_data"][unit]:
                if (not category or student["Categoría"] == category) and (
                    not matricula or str(student["Matrícula"]) == matricula
                ):
                    key = f"{student['Nombre']} {student['Apellido']}"
                    if key not in filtered_results:
                        filtered_results[key] = {
                            "id": student["Id"],
                            "matricula": student["Matrícula"],
                            "nombre": student["Nombre"],
                            "apellido": student["Apellido"],
                            "promedios": {},
                            "categoria": student["Categoría"],
                        }
                    filtered_results[key]["promedios"][unit] = student["Promedio"]

    return jsonify(filtered_results)


@router.route("/login/moduloDocentes/filter", methods=["GET", "POST"])
def filter_students_view():
    if request.method == "GET":
        category = request.args.get("average")
        matricula = request.args.get("matricula")
    else:
        category = request.form.get("category")
        matricula = request.form.get("matricula")

    data = load_excel_data()

    filtered_results = {}
    for unit, unit_data in data.items():
        for student in unit_data:
            if (category and student.get("Categoría") == category) or (
                matricula and str(student.get("Matrícula")) == matricula
            ):
                if student["Nombre"] not in filtered_results:
                    filtered_results[student["Nombre"]] = {
                        "id": student["Id"],
                        "matricula": student["Matrícula"],
                        "nombre": student["Nombre"],
                        "apellido": student["Apellido"],
                        "promedios": {},
                        "categoria": student["Categoría"],
                    }
                filtered_results[student["Nombre"]]["promedios"][unit] = student[
                    "Promedio"
                ]

    return jsonify(filtered_results)


@router.route("/login/moduloDocentes/download/<category>")
def download_filtered(category):
    data = load_data()
    results = calculate_averages(data)
    filtered_results = filter_students(results, category)
    df = pd.DataFrame(filtered_results).T

    excel_path = os.path.join(
        app.config["UPLOAD_FOLDER"], f"filtered_students_{category}.xlsx"
    )
    df.to_excel(excel_path, index=True)

    return send_file(excel_path, as_attachment=True)


@router.route("/login/moduloDocentes/download_filtered_pdf", methods=["POST"])
def download_filtered_pdf():
    filtered_data = request.json

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Resultados Filtrados", ln=True, align="C")
    pdf.ln(10)

    headers = [
        "Id",
        "Matrícula",
        "Nombre",
        "Apellido",
        "Promedio U1",
        "Promedio U2",
        "Promedio U3",
        "Categoría",
    ]
    for header in headers:
        pdf.cell(25, 10, header, border=1)
    pdf.ln()

    for student in filtered_data:
        pdf.cell(25, 10, str(student["Id"]), border=1)
        pdf.cell(25, 10, str(student["Matricula"]), border=1)
        pdf.cell(25, 10, student["Nombre"], border=1)
        pdf.cell(25, 10, student["Apellido"], border=1)
        pdf.cell(25, 10, str(student["Promedios"].get("Unidad1", "N/A")), border=1)
        pdf.cell(25, 10, str(student["Promedios"].get("Unidad2", "N/A")), border=1)
        pdf.cell(25, 10, str(student["Promedios"].get("Unidad3", "N/A")), border=1)
        pdf.cell(25, 10, student["Categoria"], border=1)
        pdf.ln()

    pdf_path = os.path.join(current_app.config["UPLOAD_FOLDER"], "filtered_results.pdf")
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)


REPORTES_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
REPORTES_FILE = os.path.join(REPORTES_DIR, "reportes.json")

def load_reportes():
    if os.path.exists(REPORTES_FILE):
        try:
            with open(REPORTES_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    print("El archivo JSON está vacío.")
                    return {"reportes": []}
                data = json.loads(content)
                if not isinstance(data, dict) or "reportes" not in data:
                    print("El archivo JSON no tiene el formato esperado.")
                    return {"reportes": []}
                return data
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return {"reportes": []}
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return {"reportes": []}
    else:
        print(f"El archivo {REPORTES_FILE} no existe.")
        return {"reportes": []}


def save_reportes(reportes):
    os.makedirs(REPORTES_DIR, exist_ok=True)
    with open(REPORTES_FILE, "w") as f:
        json.dump(reportes, f, indent=2)


@router.route("/login/moduloDocentes/reportes")
def reportes():
    reportes_data = load_reportes()
    return render_template(
        "tempsDocente/reportes.html",
        reportes=reportes_data.get("reportes", []),
    )


@router.route("/login/moduloDocentes/send_report", methods=["POST"])
def send_report():
    data = request.json
    reportes_data = load_reportes()

    report_id = len(reportes_data["reportes"]) + 1

    if data["type"] == "final":
        df = pd.DataFrame()
        for unit, unit_data in data["data"].items():
            df = pd.concat([df, pd.DataFrame(unit_data)], ignore_index=True)
    else:
        df = pd.DataFrame(data["data"])

    excel_filename = f"report_{report_id}_{data['type']}.xlsx"
    excel_path = os.path.join(REPORTES_DIR, excel_filename)
    df.to_excel(excel_path, index=False)

    new_report = {
        "id_reporte": report_id,
        "nombre_docente": data.get("nombre_docente", ""),
        "materia": data["subject"],
        "ciclo": data["cycle"],
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": data["type"],
        "excel_filename": excel_filename,
        # "descargar_informe": f"/login/moduloDocentes/download_report/{report_id}",
    }

    reportes_data["reportes"].append(new_report)
    save_reportes(reportes_data)

    return jsonify({"success": True, "report_id": report_id})


@router.route("/login/moduloDocentes/view_report/<int:report_id>")
def view_report(report_id):
    reportes_data = load_reportes()
    report = next((r for r in reportes_data["reportes"] if r["id"] == report_id), None)
    if report:
        return render_template("tempsDocente/view_report.html", report=report)
    else:
        return "Reporte no encontrado", 404


@router.route("/login/moduloDocentes/download_report/<int:report_id>")
def download_report(report_id):
    reportes_data = load_reportes()
    report = next(
        (r for r in reportes_data["reportes"] if r["id_reporte"] == report_id), None
    )
    if report:
        excel_path = os.path.join(REPORTES_DIR, report["excel_filename"])
        if os.path.exists(excel_path):
            return send_file(
                excel_path,
                as_attachment=True,
                download_name=report["excel_filename"],
            )
    return "Reporte no encontrado", 404

#------------MODULO DE PROYECCIONES-----------
@router.route('/carga', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            filepath = os.path.join('data', filename)
            file.save(filepath)
            return redirect(url_for('router.process_file', filename=filename))
    return render_template('tempsDocente/estudiante/alumnos.html')

@router.route('/process_file/<filename>', methods=['GET'])
def process_file(filename):
    filepath = os.path.join('data', filename)
    df = pd.read_excel(filepath)

    # Asegúrate de que las columnas existen antes de la suma
    if all(col in df.columns for col in ['AA', 'ACD', 'APE', 'EVALUACION']):
        df['TOTAL'] = df[['AA', 'ACD', 'APE', 'EVALUACION']].sum(axis=1)
        df['PROYECCION'] = 21 - df['TOTAL']
        df['PROYECCION'] = df['PROYECCION'].apply(lambda x: max(x, 0))
        df['PASAR'] = df['TOTAL'] >= 21
        df['PROYECCION_LINK'] = df.index.to_series().apply(lambda x: f'<a href="/projection/{x}">Proyección</a>')

        # Guardar datos en JSON
        grades_json = df.to_json(orient='records')
        with open('data/grades.json', 'w') as f:
            f.write(grades_json)

        # Renderizar la tabla en HTML
        return render_template('tempsDocente/estudiante/notas.html', tables=[df.to_html(classes='data', index=False, escape=False)], titles=df.columns.values)
    else:
        return "Error: El archivo Excel no contiene las columnas necesarias", 400

@router.route('/projection/<int:student_id>', methods=['GET'])
def student_projection(student_id):
    with open('data/grades.json', 'r') as f:
        grades = json.load(f)

    if 0 <= student_id < len(grades):
        student = grades[student_id]
        return render_template('tempsDocente/estudiante/proyeccion.html', student=student)
    else:
        return "Estudiante no encontrado", 404
