from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Renamed app to user_service_app
user_service_app = Flask(__name__)
CORS(user_service_app)  # Allow cross-origin requests
user_service_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_database.db'  # Changed database name
user_service_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(user_service_app)

# Renamed Person model to User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Added email field

with user_service_app.app_context():
    db.create_all()

# Renamed route and function names
@user_service_app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data.get('name'), email=data.get('email'))  # Added email field
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

@user_service_app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users]), 200

@user_service_app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    u = User.query.get(id)
    return jsonify({"id": u.id, "name": u.name, "email": u.email}) if u else (jsonify({"error": "Not found"}), 404)

@user_service_app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    u = User.query.get(id)
    if u:
        db.session.delete(u)
        db.session.commit()
        return jsonify({"msg": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    user_service_app.run(host='0.0.0.0', port=5003)  # Changed port to 5003