from sqlalchemy import or_
from models.user import User
from utils.security import hash_password,check_password
from extensions import db
from flask_jwt_extended import create_access_token, get_jwt_identity, create_refresh_token,get_jwt
from utils.token_blacklist import add_token_to_blacklist


def register_user(data):
    username = data.get('username')
    email = data.get('email')
    existing_user=User.query.filter(
        or_(
            User.username == username,
            User.email == email
        )
    ).first()
    if existing_user:
        if existing_user.username == username:
            return ({
                "success": False,
                "message": "Username already exists"
            })
        elif existing_user.email == email:
            return ({
                "success": False,
                "message": "Email already exists"
            })
        return ({
            "success": False,
            "message": "UnExpected Error."
        })
    hashed_password = hash_password(data['password'])
    new_user = User(
    username=username,
    email=email,
    password_hash=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return ({
        "success": True,
        "message": "User created successfully"
    })

def login_user(data):
    entered_password = data.get('password')
    email=data.get('email')
    user_found=User.query.filter_by(email=email).first()
    if not user_found:
        return ({
            "success": False,
            "message" : "Invalid Email or Password"
        })
    stored_password = user_found.password_hash
    verified_password=check_password(stored_password,entered_password)
    if not verified_password:
        return ({
            "success": False,
            "message" : "Invalid Email or Password"
        })
    access_token=create_access_token(identity=str(user_found.id))
    refresh_token=create_refresh_token(identity=str(user_found.id))
    return({
        "success": True,
        "message": "Successfully logged in",
        "access_token": access_token,
        "refresh_token": refresh_token
    })

def view_profile():
    user_id=int(get_jwt_identity())
    user=db.session.query(User,user_id)
    if not user:
        return ({
            "success": False,
            "message" : "User Not Found"
        }),404
    return ({
        "success": True,
        "data":{
        "id" : user.id,
        "username" : user.username,
        "email" : user.email
            }
    }),200
def delete_user():
    user_id = int(get_jwt_identity())
    user=db.session.get(User,user_id)
    if not user:
        return ({
            "success": False,
            "message": "User Not Found"
        }), 404
    jti=get_jwt()["jti"]
    add_token_to_blacklist(jti)
    db.session.delete(user)
    db.session.commit()
    return ({
        "success": True,
        "message": "User deleted successfully"
    }),200
def update_user(data):
    username=data.get('username')
    email=data.get('email')
    if not username and not email:
        return ({
            "success": False,
            "message": "No fields provided for update."
        }),400
    user_id= int(get_jwt_identity())
    user=db.session.get(User,user_id)
    if not user:
        return ({
            "success": False,
            "message": "User Not Found"
        }),404
    existing_user=db.session.query(User).filter(
        User.id!=user_id,
        or_(
        User.username == username,
        User.email == email
    )).first()
    if existing_user:
        if existing_user.username == username:
            return ({
                "success": False,
                "message": "Username already exists"
            })
        elif existing_user.email == email:
            return ({
                "success": False,
                "message": "Email already exists"
            })
        return ({
            "success": False,
            "message": "UnExpected Error."
        })
    if username:
        user.username=username
    if email:
        user.email=email
    db.session.commit()
    return ({
        "success": True,
        "message": "User updated successfully",
        "data":{
            "id" : user.id,
            "username" : user.username,
            "email" : user.email
        }
        }),200