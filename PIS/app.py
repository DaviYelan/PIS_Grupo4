from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager
from os import path
from dotenv import load_dotenv
from config.config import config

basedir = path.abspath(path.dirname('file'))
load_dotenv(path.join(basedir, 'config/.env'))

db = MySQL()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config['development'])

    db.init_app(app)

    with app.app_context():
        from routes.router import router
        app.register_blueprint(router)

        login_manager = LoginManager()
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            from models.Modelcuenta import ModelCuenta
            return ModelCuenta.get_by_id(db, id)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")