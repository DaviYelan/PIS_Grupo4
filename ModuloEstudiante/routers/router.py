from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from flask_cors import CORS
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/inicio')
def homeinicio():
    return render_template("index.html")

@router.route('/calendario')
def calendario():
    return render_template("estudiante/calendario.html")

@router.route('/')
def home():
    return render_template("index.html")