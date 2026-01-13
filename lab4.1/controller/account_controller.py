from flask import Blueprint, request, jsonify
from service.account_service import AccountService

account_bp = Blueprint('account', __name__)

@account_bp.route('/accounts', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    tags:
      - Accounts
    responses:
      200:
        description: List of users
        examples:
          application/json: [{"id":1,"username":"John"}]
    """
    users = AccountService.get_all_users()
    return jsonify(users), 200

@account_bp.route('/accounts/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID
    ---
    tags:
      - Accounts
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User found
      404:
        description: User not found
    """
    user = AccountService.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@account_bp.route('/accounts', methods=['POST'])
def add_user():
    """
    Add a new user
    ---
    tags:
      - Accounts
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [username, email, password, gender]
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
            gender:
              type: string
    responses:
      201:
        description: User created
      400:
        description: Invalid data
    """
    data = request.get_json()
    required_fields = ['username', 'email', 'password', 'gender']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields'}), 400

    user = AccountService.create_user(data)
    return jsonify(user), 201

@account_bp.route('/accounts/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update user by ID
    ---
    tags:
      - Accounts
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: User ID
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
            password:
              type: string
            gender:
              type: string
    responses:
      200:
        description: User updated
      404:
        description: User not found
    """
    data = request.get_json()
    user = AccountService.update_user(user_id, data)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@account_bp.route('/accounts/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete user by ID
    ---
    tags:
      - Accounts
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: User ID
    responses:
      200:
        description: User deleted
      404:
        description: User not found
    """
    success = AccountService.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404