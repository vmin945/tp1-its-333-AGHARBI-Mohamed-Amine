import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

# Renamed app to medical_service_app
medical_service_app = Flask(__name__)
CORS(medical_service_app)
medical_records = {}  # Renamed health_db to medical_records

# Renamed function to verify_user_exists
# Updated comments to reflect new purpose

def verify_user_exists(user_id):
    try:
        # Communication with user service via Docker host
        url = f"http://host.docker.internal:5003/users/{user_id}"
        response = requests.get(url, timeout=2)
        return response.status_code == 200
    except:
        return False

# Renamed route and function names
@medical_service_app.route('/records/<int:user_id>', methods=['GET'])
def get_medical_record(user_id):
    # Returns medical data or default values if empty
    data = medical_records.get(user_id, {"weight": "-", "height": "-"})
    return jsonify(data), 200

@medical_service_app.route('/records/<int:user_id>', methods=['POST'])
def save_medical_record(user_id):
    if not verify_user_exists(user_id):
        return jsonify({"error": "User does not exist"}), 404
    medical_records[user_id] = request.json
    return jsonify({"status": "Data saved"}), 200

@medical_service_app.route('/records/<int:user_id>', methods=['DELETE'])
def delete_medical_record(user_id):
    if user_id in medical_records:
        del medical_records[user_id]
    return jsonify({"status": "Medical record deleted"}), 200

if __name__ == '__main__':
    medical_service_app.run(host='0.0.0.0', port=5004)  # Changed port to 5004