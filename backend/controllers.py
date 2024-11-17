from flask import Flask, jsonify, request
import os
import services  

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.get_json()
    result = services.create_customer(data)  
    return jsonify(result), 201

@app.route('/customer/<customer_id>', methods=['GET'])
def read_customer(customer_id):
    result = services.get_customer(customer_id)  
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Customer not found"}), 404

@app.route('/customer/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    result = services.update_customer(customer_id, data)  
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Update failed"}), 400

@app.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if services.delete_customer(customer_id):  
        return jsonify({"success": "Customer deleted"}), 200
    else:
        return jsonify({"error": "Deletion failed"}), 400

@app.route('/customer/<customer_id>/deals', methods=['POST'])
def manage_deals(customer_id):
    data = request.get_json()
    result = services.manage_deals(customer_id, data)  
    if result:
        return jsonify(result), 201
    else:
        return jsonify({"error": "Failed to manage deals"}), 400

@app.route('/customer/<customer_id>/interactions', methods=['POST'])
def track_interactions(customer_id):
    data = request.get_json()
    result = services.track_interactions(customer_id, data)  
    if result:
        return jsonify(result), 201
    else:
        return jsonify({"error": "Failed to track interactions"}), 400

if __name__ == '__main__':
    app.run(debug=True)