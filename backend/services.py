import os
from datetime import datetime
import sqlite3
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

DATABASE_URL = 'your_database_url_here.db'
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()

def create_customer(name, email):
    try:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        logging.info("Customer created: %s, %s", name, email)
        return {"status": "success", "message": "Customer created successfully."}
    except Exception as e:
        logging.error("Error creating customer: %s", e)
        return {"status": "error", "message": str(e)}

def read_customer_by_id(customer_id):
    try:
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        customer = cursor.fetchone()
        if customer:
            logging.info("Customer retrieved: %s", customer_id)
            return {"status": "success", "data": customer}
        else:
            logging.warning("Customer not found: %s", customer_id)
            return {"status": "error", "message": "Customer not found."}
    except Exception as e:
        logging.error("Error reading customer by ID: %s", e)
        return {"status": "error", "message": str(e)}
    
def update_customer(customer_id, name=None, email=None):
    try:
        updates = []
        params = []
        if name:
            updates.append("name = ?")
            params.append(name)
        if email:
            updates.append("email = ?")
            params.append(email)
        params.append(customer_id)
        cursor.execute(f"UPDATE customers SET {', '.join(updates)} WHERE id = ?", params)
        conn.commit()
        logging.info("Customer updated: %s", customer_id)
        return {"status": "success", "message": "Customer updated successfully."}
    except Exception as e:
        logging.error("Error updating customer: %s", e)
        return {"status": "error", "message": str(e)}

def delete_customer(customer_id):
    try:
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        logging.info("Customer deleted: %s", customer_id)
        return {"status": "success", "message": "Customer deleted successfully."}
    except Exception as e:
        logging.error("Error deleting customer: %s", e)
        return {"status": "error", "message": str(e)}

def associate_deal_with_customer(deal_id, customer_id):
    try:
        cursor.execute("UPDATE deals SET customer_id = ? WHERE id = ?", (customer_id, deal_id))
        conn.commit()
        logging.info("Deal %s associated with customer %s successfully.", deal_id, customer_id)
        return {"status": "success", "message": "Deal associated with customer successfully."}
    except Exception as e:
        logging.error("Error associating deal with customer: %s", e)
        return {"status": "error", "message": str(e)}

def update_deal_status(deal_id, status):
    try:
        cursor.execute("UPDATE deals SET status = ? WHERE id = ?", (status, deal_id))
        conn.commit()
        logging.info("Deal status updated: %s, %s", deal_id, status)
        return {"status": "success", "message": "Deal status updated successfully."}
    except Exception as e:
        logging.error("Error updating deal status: %s", e)
        return {"status": "error", "message": str(e)}

def add_interaction(customer_id, interaction_type, details, date=None):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor.execute("INSERT INTO interactions (customer_id, interaction_type, details, date) VALUES (?, ?, ?, ?)", (customer_id, interaction_type, details, date))
        conn.commit()
        logging.info("Interaction added for customer %s", customer_id)
        return {"status": "success", "message": "Interaction added successfully."}
    except Exception as e:
        logging.error("Error adding interaction: %s", e)
        return {"status": "error", "message": str(e)}

def view_interactions(customer_id):
    try:
        cursor.execute("SELECT * FROM interactions WHERE customer_id = ?", (customer_id,))
        interactions = cursor.fetchall()
        if interactions:
            logging.info("Interactions retrieved for customer %s", customer_id)
            return {"status": "success", "data": interactions}
        else:
            logging.warning("No interactions found for customer %s", customer_id)
            return {"status": "error", "message": "No interactions found for this customer."}
    except Exception as e:
        logging.error("Error viewing interactions: %s", e)
        return {"status": "error", "message": str(e)}

def edit_interaction(interaction_id, interaction_type=None, details=None, date=None):
    try:
        updates = []
        params = []
        if interaction_type:
            updates.append("interaction_type = ?")
            params.append(interaction_type)
        if details:
            updates.append("details = ?")
            params.append(details)
        if date:
            updates.append("date = ?")
            params.append(date)
        params.append(interaction_id)
        cursor.execute(f"UPDATE interactions SET {', '.join(updates)} WHERE id = ?", params)
        conn.commit()
        logging.info("Interaction updated: ID %s", interaction_id)
        return {"status": "success", "message": "Interaction updated successfully."}
    except Exception as e:
        logging.error("Error editing interaction: %s", e)
        return {"status": "error", "message": str(e)}