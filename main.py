from flask import Flask, jsonify
from database import initialize_db
from config import Config
from controllers import configure_routes
import os
import sys

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': Config.DATABASE_URI
}

try:
    initialize_db(app)
    configure_routes(app)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=Config.PORT)

    print(f"Server started successfully on port {Config.PORT}")

except Exception as e:
    print(f"Error starting the server: {str(e)}")
    sys.exit(1)