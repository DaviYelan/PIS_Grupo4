from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from flask_cors import CORS
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion

@router.route('/calendario')
def calendario():
    return render_template("estudiante/calendario.html")

@router.route('/')
def home():
    return render_template("index.html")

@router.route('/principal')
def principal():
    return render_template("index.html")

@router.route('/notificacion')
def notificacion():
    return render_template("estudiante/notificaciones.html")

@router.route('/cursos')
def cursos():
    return render_template("estudiante/cursos.html")