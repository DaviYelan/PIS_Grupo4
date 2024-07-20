from flask import Blueprint, render_template, redirect, request, flash, abort
from controllers.estudianteDaoControl import EstudianteDaoControl
from controllers.personaDaoControl import PersonaDaoControl
from flask_login import logout_user, login_required, login_user, LoginManager
from app import db
from models.Modelcuenta import ModelCuenta
from models.cuenta import Cuenta
from controllers.docenteDaoControl import DocenteDaoControl
from controllers.materiaDaoControl import MateriaDaoControl


router = Blueprint('router', __name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return ModelCuenta.get_by_id(db, id)


#-------------LOGIN--------------
@router.route('/')
def home():
    return redirect("/login")

@router.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cuenta = Cuenta(0, username, password)
        logged_user = ModelCuenta.login(db, cuenta)
        if logged_user:
            if logged_user.clave:
                login_user(logged_user)
                if logged_user.role == 'admin':
                    return redirect("/login/moduloAdmin")
                elif logged_user.role == 'estudiante':
                    return redirect("/login/moduloEstudiantes")
                elif logged_user.role == 'docente':
                    return redirect("/login/moduloDocentes")
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

@router.route('/login/moduloAdmin')
def moduloAdmin():
    return render_template('tempsAdmin/index.html')

@router.route('/registrarEstudiantes')
def ver_guardado():
    return render_template('tempsAdmin/estudiante/registrarEstudiante.html')

#----------------------SECCION ESTUDIANTE--------------------------------------------
@router.route('/accionEstudi')
def ver_opcionesEstud():
    return render_template('tempsAdmin/estudiante/accionEstudi.html')

#LISTA DE ESTUDIANTES
@router.route('/listaEstudiante')
def ver_estudiantes():
    estudiante = EstudianteDaoControl()
    return render_template('tempsAdmin/estudiante/listaEstudiante.html', lista = estudiante.to_dic())

#MOSTRAR LISTA DE ESTUDIANTES
@router.route('/estudiantes/ver')
def mostrar():
    return render_template('tempsAdmin/estudiante/registrarEstudi.html')

#EDITAR ESTUDIANTES
@router.route('/registrar/editar/<pos>')
def ver_editar(pos):
    fd = EstudianteDaoControl()
    nene = fd._list().get(int(pos)-1)
    return render_template("tempsAdmin/estudiante/editarEstudi.html", data=nene)


@router.route('/registrar/guardar', methods=['POST'])
def guardar_estudiante():
    est = EstudianteDaoControl()
    est._estudiante._id = request.form['id']
    est._estudiante._nombre = request.form['nombre']
    est._estudiante._apellido = request.form['apellido']
    est._estudiante._fecha = request.form['fecha']
    est._estudiante._genero = request.form['genero']
    est._estudiante._telefono = request.form['telefono']
    est._estudiante._correo = request.form['correo']
    est._estudiante._orden = request.form['orden']
    est._estudiante._ciclo = request.form['ciclo']
    est.save
    return redirect('/listaEstudiante', code = 302)

@router.route('/registrar/modificar', methods=['POST'], )
def modificar_estudiante():
    et= EstudianteDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = et._list().get(int(pos)-1)
    et._estudiante._nombre = data['nombre']
    et._estudiante._apellido = data['apellido']
    et._estudiante._fecha = request.form['fecha']
    et._estudiante._genero = request.form['genero']
    et._estudiante._telefono = request.form['telefono']
    et._estudiante._correo = request.form['correo']
    et._estudiante._orden = request.form['orden']
    et._estudiante._ciclo = request.form['ciclo']
    et.merge(int(pos))
    return redirect("/listaEstudiante", code=302)

########         Seccion Docente      ###################
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
    docente = DocenteDaoControl()
    return render_template('tempsAdmin/docente/lista.html', lista=docente.to_dic())

#MOSTRAR LISTA DE DOCENTES
@router.route('/docentes/ver')
def ver():
    return render_template('tempsAdmin/docente/registrar.html')

#EDITAR DOCENTES
@router.route('/registrarDocentes/editar/<pos>')
def ver_edita(pos):
    dc = DocenteDaoControl()
    nene = dc._list().get(int(pos)-1)
    return render_template("tempsAdmin/docente/editarDocen.html", data=nene)

#guardar docentes
@router.route('/registrarDocentes/guardar', methods=['POST'])
def guardar_docentes():
    est = DocenteDaoControl()
    est._docente._id = request.form['id']
    est._docente._nombre = request.form['nombre']
    est._docente._apellido = request.form['apellido']
    est._docente._fecha = request.form['fecha']
    est._docente._genero = request.form['genero']
    est._docente._telefono = request.form['telefono']
    est._docente._correo = request.form['correo']
    est._docente._tipoIdentificacion = request.form['tipoIdentificacion']
    est._docente._tituloCuartoNivel = request.form['tituloCuartoNivel']
    est._docente._especialidad = request.form['especialidad']
    est._docente._cubiculo = request.form['cubiculo']
    est.save
    return redirect('/listaDocente', code = 302)


@router.route('/registrarDocentes/modificar', methods=['POST'], )
def modificar_docente():
    mdc= DocenteDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = mdc._list().get(int(pos)-1)
    mdc._docente = nene
    mdc._docente._ = data['nombre']
    mdc._docente._apellido = data['apellido']
    mdc._docente._direccion = data['direccion']
    mdc._docente._fechaNacimiento = data['fechaNacimiento']
    mdc._docente._genero = data['genero']
    mdc._docente._telefono = data['telefono']
    mdc._docente._tipoIdentificacion = data['tipoIdentificacion']
    mdc._docente._cedula = data['cedula']
    mdc.merge(int(pos))
    return redirect("/listaDocentes", code=302)


########         Seccion Materia      ###################

@router.route('/accionMateria')
def ver_opcionesMaterias():
    return render_template('tempsAdmin/materia/accionMateria.html')


@router.route('/registrarMateria')
def ver_guardarMateria():
    return render_template('tempsAdmin/materia/registrarMateria.html')


@router.route('/listaMateria')
def ver_materias():
    materia = MateriaDaoControl()
    return render_template('tempsAdmin/materia/listaMateria.html', lista = materia.to_dic())


@router.route('/registrarMateria/editar/<pos>')
def ver_editarMateria(pos):
    mdc = MateriaDaoControl()
    nene = mdc._list().get(int(pos)-1)
    return render_template("tempsAdmin/materia/editarMateria.html", data=nene)


@router.route('/registrarMateria/guardar', methods=['POST'])
def guardar_materias():
    mdc = MateriaDaoControl()
    mdc._materia._nombre = request.form['nombre']
    mdc._materia._codigo = request.form['codigo']
    mdc._materia._horaSemanal = request.form['horaSemanal']
    mdc._materia._nombCiclo = request.form['nombCiclo']
    mdc.save
    return redirect('tempsAdmin/materia/listaMateria', code = 302)


@router.route('/registrarMateria/modificar', methods=['POST'], )
def modificar_materia():
    mdc= MateriaDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = mdc._list().get(int(pos)-1)
    mdc._materia = nene
    mdc._materia._nombre = data['nombre']
    mdc._materia._codigo = data['codigo']
    mdc._materia._horaSemanal = data['horaSemanal']
    mdc._materia._nombCiclo = data['nombCiclo']
    
    mdc.merge(int(pos))
    return redirect("/listaMateria", code=302)



#---------------MODULO DE DOCENTE-----------------

@router.route('/login/moduloDocentes')
def moduloDocente():
    return render_template('tempsDocente/index.html')

@router.route('/alumnos')
def alumnos():
    return render_template('tempsDocente/estudiante/alumnos.html')
#---------------MODULO DE ESTUDIANTE-----------------


@router.route('/calendario')
def calendario():
    return render_template("tempsEstudiante/estudiante/calendario.html")

@router.route('/')
def homeEstudiante():
    return render_template("tempsEstudiante/index.html")

@router.route('/login/moduloEstudiantes')
def moduloEstudiante():
    return render_template("tempsEstudiante/index.html")

@router.route('/notificacion')
def notificacion():
    return render_template("tempsEstudiante/estudiante/notificaciones.html")

@router.route('/cursos')
def cursos():
    return render_template("tempsEstudiante/estudiante/cursos.html")

@router.route('/progreso')
def progreso():
    return render_template("tempsEstudiante/estudiante/progreso.html")

@router.route('/proyeccion')
def proyeccion():
    return render_template("tempsEstudiante/estudiante/proyeccion.html")
#------------MODULO DE MENSAJES-----------
@router.route('/registro')
def registro():
    return render_template('tempsMensajes/registro.html')

@router.route('/sala')
@login_required
def sala():
    return render_template('tempsMensajes/sala.html')