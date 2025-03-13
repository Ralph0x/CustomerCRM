import os
from datetime import datetime
import sqlite3
conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()

def create_customer(name, email):
    try:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        return {"status": "success", "message": "Customer created successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def read_customer_by_id(customer_id):
    try:
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        customer = cursor.fetchone()
        if customer:
            return {"status": "success", "data": customer}
        else:
            return {"status": "error", "message": "Customer not found."}
    except Exception as e:
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
        return {"status": "success", "message": "Customer updated successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def delete_customer(customer_id):
    try:
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        return {"status": "success", "message": "Customer deleted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)"}

def associate_deal_with_customer(deal_id, customer_id):
    try:
        cursor.execute("UPDATE deals SET customer_id = ? WHERE id = ?", (customer_id, deal_id))
        conn.commit()
        return {"status": "success", "message": "Deal associated with customer successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def update_deal_status(deal_id, status):
    try:
        cursor.execute("UPDATE deals SET status = ? WHERE id = ?", (status, deal_id))
        conn.commit()
        return {"status": "success", "message": "Deal status updated successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def add_interaction(customer_id, interaction_type, details, date=None):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor.execute("INSERT INTO interactions (customer_id, interaction_type, details, date) VALUES (?, ?, ?, ?)", (customer_id, interaction_type, details, date))
        conn.commit()
        return {"status": "success", "message": "Interaction added successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def view_interactions(customer_id):
    try:
        cursor.execute("SELECT * FROM interactions WHERE customer_id = ?", (customer_id,))
        interactions = cursor.fetchall()
        if interactions:
            return {"status": "success", "data": interactions}
        else:
            return {"status": "error", "message": "No interactions found for this customer."}
    except Exception as e:
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
        return {"status": "success", "message": "Interaction updated successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}