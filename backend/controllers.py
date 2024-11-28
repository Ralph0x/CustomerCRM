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

@app.route('/customers/batch', methods=['POST'])
def create_customers_batch():
    data = request.get_json()
    results = services.create_customers_batch(data)  # Assumes implementation of batch create in services
    return jsonify(results), 201

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

@app.route('/customers/batch', methods=['PUT'])
def update_customers_batch():
    data = request.get_json()
    results = services.update_customers_batch(data)  # Assumes implementation of batch update in services
    return jsonify(results), 200

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

@app.route('/customers/deals/batch', methods=['POST'])
def manage_deals_batch():
    data = request.get_json()
    results = services.manage_deals_batch(data)  # Assumes implementation of batch deal management in services
    return jsonify(results), 201

@app.route('/customer/<customer_id>/interactions', methods=['POST'])
def track_interactions(customer_id):
    data = request.get_json()
    result = services.track_interactions(customer_id, data)  
    if result:
        return jsonify(result), 201
    else:
        return jsonify({"error": "Failed to track interactions"}), 400

@app.route('/customers/interactions/batch', methods=['POST'])
def track_interactions_batch():
    data = request.get_json()
    results = services.track_interactions_batch(data)  # Assumes implementation of batch interaction tracking in services
    return jsonify(results), 201

if __name__ == '__main__':
    app.run(debug=True)