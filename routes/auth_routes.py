from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity,create_access_token
from utils.token_blacklist import add_token_to_blacklist
from utils.validation import validate_registration_data
from services.auth_service import register_user,login_user,view_profile,delete_user,update_user,change_password
auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/register',methods=['POST'])
def register():
    """
    Register a new user.

    ---
    summary: Register a new user
    description: Creates a new user account after validating the username, email, and password. Passwords are securely hashed before being stored in the database.
    tags:
      - Authentication

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
              example: hariharan
            email:
              type: string
              example: hari@gmail.com
            password:
              type: string
              example: Password@123

    responses:
      200:
        description: User registered successfully.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: true
            message:
              type: string
              example: User created successfully

      400:
        description: Validation failed or user already exists.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: false
            message:
              type: string
              example: Username already exists
    """
    data=request.get_json()
    result = validate_registration_data(data)
    if not result['success']:
        return jsonify(result),400
    result = register_user(data)
    return jsonify(result),201

@auth_bp.route('/login',methods=['POST'])
def login():
    """
    Login user.

    ---
    summary: Login user
    description: Authenticates the user using email and password. Returns an access token and refresh token upon successful authentication.
    tags:
      - Authentication

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: hari@gmail.com
            password:
              type: string
              example: Password@123

    responses:
      200:
        description: Login successful.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: true
            message:
              type: string
              example: Successfully logged in
            access_token:
              type: string
            refresh_token:
              type: string

      400:
        description: Invalid credentials.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: false
            message:
              type: string
              example: Invalid Email or Password
    """
    data=request.get_json()
    result= login_user(data)
    if not result['success']:
        return jsonify(result),400
    return jsonify(result),200

@auth_bp.route('/profile', methods=["GET"])
@jwt_required()
def profile():
    """
    View user profile.

    ---
    summary: View profile
    description: Returns the authenticated user's profile information.
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: Profile retrieved successfully.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: true
            data:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: hariharan
                email:
                  type: string
                  example: hari@gmail.com

      401:
        description: Unauthorized.

      404:
        description: User not found.
    """
    result,status=view_profile()
    return jsonify(result),status

@auth_bp.route('/logout', methods=["POST"])
@jwt_required()
def logout():
    """
    Logout user.

    ---
    summary: Logout user
    description: Revokes the current access token by adding its JTI to the blacklist.
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: Logged out successfully.

      401:
        description: Unauthorized.
    """
    jti = get_jwt()['jti']
    result,status=add_token_to_blacklist(jti)
    return jsonify(result),status

@auth_bp.route('/refresh', methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """
    Refresh access token.

    ---
    summary: Refresh access token
    description: Generates a new access token using a valid refresh token.
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: New access token generated.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: true
            access_token:
              type: string

      401:
        description: Invalid or expired refresh token.
    """
    user_id=get_jwt_identity()
    access_token=create_access_token(identity=user_id)
    return jsonify({
        "success": True,
        "access_token": access_token
    }),200

@auth_bp.route('/profile', methods=["DELETE"])
@jwt_required()
def delete():
    """
    Delete user account.

    ---
    summary: Delete user account
    description: Permanently deletes the authenticated user's account.
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: User deleted successfully.

      401:
        description: Unauthorized.

      404:
        description: User not found.
    """
    result,status=delete_user()
    return jsonify(result),status
@auth_bp.route("/profile",methods=["PUT"])
@jwt_required()
def update():
    """
    View user profile.

    ---
    summary: View profile
    description: Returns the authenticated user's profile information.
    tags:
      - Authentication

    security:
      - Bearer: []

    responses:
      200:
        description: Profile retrieved successfully.
        schema:
          type: object
          properties:
            success:
              type: boolean
              example: true
            data:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: hariharan
                email:
                  type: string
                  example: hari@gmail.com

      401:
        description: Unauthorized.

      404:
        description: User not found.
    """
    data=request.get_json()
    result,status=update_user(data)
    return jsonify(result),status
@auth_bp.route("/profile/password",methods=["PUT"])
@jwt_required()
def update_password():
    """
    Change password.

    ---
    summary: Change user password
    description: Changes the authenticated user's password after verifying the current password.
    tags:
      - Authentication

    security:
      - Bearer: []

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - current_password
            - new_password
          properties:
            current_password:
              type: string
              example: Password@123
            new_password:
              type: string
              example: NewPassword@123

    responses:
      200:
        description: Password changed successfully.

      400:
        description: Invalid request.

      401:
        description: Current password is incorrect.

      404:
        description: User not found.
    """
    data=request.get_json()
    result,status=change_password(data)
    return jsonify(result),status