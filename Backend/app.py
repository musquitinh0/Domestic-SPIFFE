from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import secrets 

import urllib.parse as up

app = Flask(__name__)

secret_key = secrets.token_hex(32)
app.config['JWT_SECRET_KEY'] = secret_key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

jwt = JWTManager(app)
CORS(app)

if __name__ == '__main__':
    from auth import auth_routes

    app.register_blueprint(auth_routes, url_prefix='/api')

    app.run()