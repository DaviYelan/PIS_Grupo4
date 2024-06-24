from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        from routes.router import router
        app.register_blueprint(router)
    return app

# Para ejecutar la aplicación directamente desde app.py
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")

