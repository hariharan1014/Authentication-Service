from flask import Flask
from config import Config
from extensions import db,bcrypt,jwt
from routes.auth_routes import auth_bp
from utils.token_blacklist import is_token_blacklisted
app=Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header,jwt_payload):
    jti=jwt_payload["jti"]
    return is_token_blacklisted(jti)

app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)