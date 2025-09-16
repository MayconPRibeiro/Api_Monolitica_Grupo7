from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Importar modelos para registrar no SQLAlchemy
    from models import professor, aluno, turma
    with app.app_context():
        db.create_all()

    # Registrar rotas
    from routes import register_routes
    register_routes(app)

    # Swagger
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Flask MVC API"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
