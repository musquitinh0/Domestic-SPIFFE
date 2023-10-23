import random
from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token
from flask_cors import cross_origin

users = []

auth_routes = Blueprint('auth_routes', __name__)

class User:
    def __init__(self, username, password, data, id):
        self.username = username
        self.password = password
        self.data = data
        self.id = id
    

@auth_routes.route('/', methods=['GET'])
@cross_origin()
def test():
    return 'works'

@auth_routes.route('/register', methods=['POST'])
@cross_origin()
def register():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    data = data.get('data')
    id = len(users) + 1

    user = User(username = username, password = password, data = data, id = id)

    users.append(user)

    return jsonify({'message': 'cadastro feito'}), 20



@auth_routes.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()

    # Extract email and password from request
    username = data.get('username')
    password = data.get('password')

    usuario = {}

    for user in users:
        if user.username == username and user.password == password:
            usuario = user

    if not usuario:
        return jsonify({'error': 'Invalid email or password'}), 401
    
    # Generate access token
    access_token = access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200