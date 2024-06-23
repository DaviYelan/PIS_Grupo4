from flask import Flask, redirect, render_template, request, flash
from flask_login import logout_user, login_required, login_user, LoginManager
from flask_mysqldb import MySQL
from config import config
from models.Modelcuenta import ModelCuenta
from models.entities.cuenta import Cuenta

app = Flask(__name__)
app.config.from_object(config['development'])

# Configuración de la base de datos MySQL
db = MySQL(app)

# Configuración del LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return ModelCuenta.get_by_id(db, id)

@app.route('/')
def home():
    return redirect("/home")

@app.route('/home')
def autenticacion():
    return render_template("home/home.html")

@app.route('/about')
def about():
    return render_template("complements/about.html")

@app.route('/contact')
def contact():
    return render_template("complements/contact.html")

@app.route('/example')
@login_required
def example():
    return render_template("exampleLogin.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cuenta = Cuenta(0, username, password)
        logged_user = ModelCuenta.login(db, cuenta)
        if logged_user:
            if logged_user.clave:
                login_user(logged_user)  # Marca al usuario como autenticado
                return redirect("/example")
            else:
                flash("Usuario o contraseña incorrectos")
        else:
            flash("Usuario no encontrado")
    return render_template("auth/login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

################# Conexion de modulos ######################

@app.route('/modulo/estudiante')
@login_required # Solo usuarios autenticados pueden acceder a esta ruta
def modulo_estudiante(): 
    return render_template("complements/js.html")

@app.route('/modulo/docente')
@login_required
def modulo_docente():
    return render_template("modulos/moduloDocentes.html")





if __name__ == '__main__':
    app.run()

