from flask import Flask, g
import cx_Oracle # type: ignore
from flask_login import LoginManager # type: ignore
from os import path
from dotenv import load_dotenv
from config.config import config

# Configuración del entorno
basedir = path.abspath(path.dirname(__file__))  
load_dotenv(path.join(basedir, 'config/.env'))

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config['development'])
    dsn_tns = cx_Oracle.makedsn(app.config['ORACLE_HOST'], app.config['ORACLE_PORT'], app.config['ORACLE_SID'])

    @app.before_request
    def before_request():
        if 'db' not in g:
            g.db = cx_Oracle.connect(user=app.config['ORACLE_USER'], password=app.config['ORACLE_PASSWORD'], dsn=dsn_tns)

    @app.teardown_request
    def teardown_request(exception):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    with app.app_context():
        from routes.router import router
        app.register_blueprint(router)

        login_manager = LoginManager()
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            from models.Modelcuenta import ModelCuenta
            return ModelCuenta.get_by_id(g.db, id)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
