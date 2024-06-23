from flask import Blueprint, jsonify, abort, request, render_template, redirect 

from src.app import app

router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@app.route('/')
def home():
    return redirect("/home", code=302)

@app.route('/home')
def autentificacion():
    return render_template("home/home.html")

@router.route('/about')
def about():
    return render_template("complements/about.html")

@router.route('/contact')
def contact():
    return render_template("complements/contact.html")

@router.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

    
#lista personas
@router.route('/personas')
def lista_personas():
    pd = PersonaDaoControl()
    return render_template("nene/lista.html", lista=pd.to_dict())

#Lista personas
@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")\

#Lista personas
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("nene/editar.html", data = nene )

#ELIMINAR PERSONA
# @router.route('/personas/editar/<id>')
# def eliminar_persona(id):
#     pd = PersonaDaoControl()
#     pd.delete(int(id))  # Aquí solo necesitas el id, no es necesario restar 1
#     return redirect("/personas", code=302)

#guardar personas
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)

@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.merge(int(pos) -1)
    return redirect("/personas", code=302)

