from flask import Blueprint,request, render_template, redirect
from control.docenteDaoControl import docenteDaoControl
from control.estudianteDaoControl import estudianteDaoControl
from control.materiaDaoControl import materiaDaoControl
#import json

router = Blueprint('api', __name__)

@router.route('/')
def home():
    return render_template('index.html')

@router.route('/registrarEstudiantes')
def ver_guardado():
    return render_template('estudiante/registrarEstudiante.html')

@router.route('/accionEstudi')
def ver_opcionesEstud():
    return render_template('estudiante/accionEstudi.html')

@router.route('/listaEstudiante')
def ver_estudiantes():
    estudiante = estudianteDaoControl()
    return render_template('estudiante/listaEstudiante.html', lista = estudiante.to_dic())



@router.route('/registrar/editar/<pos>')
def ver_editar(pos):
    fd = estudianteDaoControl()
    nene = fd._list().get(int(pos)-1)
    return render_template("estudiante/editarEstudi.html", data=nene)


@router.route('/registrar/guardar', methods=['POST'])
def guardar_estudiante():
    est = estudianteDaoControl()
    est._estudiante._nombre = request.form['nombre']
    est._estudiante._apellido = request.form['apellido']
    est._estudiante._direccion = request.form['direccion']
    est._estudiante._fechaNacimiento = request.form['fechaNacimiento']
    est._estudiante._genero = request.form['genero']
    est._estudiante._telefono = request.form['telefono']
    est._estudiante._tipoIdentificacion = request.form['tipoIdentificacion']
    est._estudiante._cedula = request.form['cedula']
    est.save
    return redirect('/listaEstudiante', code = 302)


@router.route('/registrar/eliminar')
def eliminar_historiales():
    estud = estudianteDaoControl()
    estud.clear_all_retenciones()
    return redirect('/', code=302)




@router.route('/registrar/modificar', methods=['POST'], )
def modificar_estudiante():
    et= estudianteDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = et._list().get(int(pos)-1)
    et._estudiante = nene
    et._estudiante._nombre = data['nombre']
    et._estudiante._apellido = data['apellido']
    et._estudiante._direccion = data['direccion']
    et._estudiante._fechaNacimiento = data['fechaNacimiento']
    et._estudiante._genero = data['genero']
    et._estudiante._telefono = data['telefono']
    et._estudiante._tipoIdentificacion = data['tipoIdentificacion']
    et._estudiante._cedula = data['cedula']
    et.merge(int(pos))
    return redirect("/listaEstudiante", code=302)

########         Seccion Docente      ###################

@router.route('/registrarDocentes')
def ver_guardar():
    return render_template('docente/registrarDocente.html')

@router.route('/accionDocente')
def ver_opcionesDocen():
    return render_template('docente/accionDocen.html')

@router.route('/listaDocentes')
def ver_docentes():
    docente = docenteDaoControl()
    return render_template('docente/listaDocen.html', lista = docente.to_dic())



@router.route('/registrarDocentes/editar/<pos>')
def ver_edita(pos):
    dc = docenteDaoControl()
    nene = dc._list().get(int(pos)-1)
    return render_template("docente/editarDocen.html", data=nene)


@router.route('/registrarDocentes/guardar', methods=['POST'])
def guardar_docentes():
    ddc = docenteDaoControl()
    ddc._docente._nombre = request.form['nombre']
    ddc._docente._apellido = request.form['apellido']
    ddc._docente._direccion = request.form['direccion']
    ddc._docente._fechaNacimiento = request.form['fechaNacimiento']
    ddc._docente._genero = request.form['genero']
    ddc._docente._telefono = request.form['telefono']
    ddc._docente._tipoIdentificacion = request.form['tipoIdentificacion']
    ddc._docente._cedula = request.form['cedula']
    ddc.save
    return redirect('/listaDocentes', code = 302)




@router.route('/registrarDocentes/modificar', methods=['POST'], )
def modificar_docente():
    mdc= docenteDaoControl()
    data = request.form
    pos = data["id"]
    print("-----------------"+data["id"])
    nene = mdc._list().get(int(pos)-1)
    mdc._docente = nene
    mdc._docente._nombre = data['nombre']
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
    return render_template('materia/accionMateria.html')


@router.route('/registrarMateria')
def ver_guardarMateria():
    return render_template('materia/registrarMateria.html')



@router.route('/listaMateria')
def ver_materias():
    materia = materiaDaoControl()
    return render_template('materia/listaMateria.html', lista = materia.to_dic())



@router.route('/registrarMateria/editar/<pos>')
def ver_editarMateria(pos):
    mdc = materiaDaoControl()
    nene = mdc._list().get(int(pos)-1)
    return render_template("materia/editarMateria.html", data=nene)


@router.route('/registrarMateria/guardar', methods=['POST'])
def guardar_materias():
    mdc = materiaDaoControl()
    mdc._materia._nombre = request.form['nombre']
    mdc._materia._codigo = request.form['codigo']
    mdc._materia._horaSemanal = request.form['horaSemanal']
    mdc._materia._nombCiclo = request.form['nombCiclo']
    mdc.save
    return redirect('materia/listaMateria', code = 302)




@router.route('/registrarMateria/modificar', methods=['POST'], )
def modificar_materia():
    mdc= materiaDaoControl()
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