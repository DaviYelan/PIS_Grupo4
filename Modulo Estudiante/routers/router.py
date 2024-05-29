from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from flask_cors import CORS
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/')
def home():
    return render_template("template.html")