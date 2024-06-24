from flask import Blueprint, render_template, request
from flask_cors import CORS

router = Blueprint('router', __name__)
CORS(router)  # Configura CORS para este blueprint específico

@router.route('/')
def home():
    return render_template('index.html')

@router.route('/registro')
def registro():
    return render_template('registro.html')

@router.route('/sala')
def sala():
    return render_template('sala.html')