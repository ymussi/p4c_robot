from flask import Flask, Blueprint
from flask_cors import CORS
from api import api
from api.robot.viewer import ns as login


def create_app(config_filename=None):
    app = Flask(__name__)
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(login, '/login')
    app.register_blueprint(blueprint)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    return app


app = create_app()


if __name__ == '__main__':
    app = create_app()
    app.run("0.0.0.0", 5000, True)
