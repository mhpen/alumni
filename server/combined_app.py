import os
import sys
from flask import Flask, send_from_directory, jsonify, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Add current directory to path to ensure imports work in Docker
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if current_dir not in sys.path:
    sys.path.append(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Import the blueprints directly instead of the app
try:
    from src.routes.admin_routes import admin_bp
    from src.routes.analytics_routes import analytics_bp
    from src.routes.prediction_routes import prediction_bp
except ImportError:
    # Try alternative import paths for Docker environment
    from routes.admin_routes import admin_bp
    from routes.analytics_routes import analytics_bp
    from routes.prediction_routes import prediction_bp

# Create a new Flask app to serve both the API and the React frontend
combined_app = Flask(__name__, static_folder='../client/build')

# Configure MongoDB (copied from app.py)
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure CORS
CORS(combined_app)

# Configure JWT
combined_app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_super_secret_key_for_jwt_tokens')
jwt = JWTManager(combined_app)

# Configure MongoDB
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement')
database_name = os.getenv('DATABASE_NAME', 'alumni_management')
client = MongoClient(mongodb_uri)
db = client[database_name]
combined_app.config['DATABASE'] = db

# Register the blueprints directly with the /api prefix
combined_app.register_blueprint(admin_bp, url_prefix='/api')
combined_app.register_blueprint(analytics_bp, url_prefix='/api')
combined_app.register_blueprint(prediction_bp, url_prefix='/api')

# API home route
@combined_app.route('/api')
def api_home():
    return jsonify({'message': 'Alumni Management System API'})

# Health check endpoint
@combined_app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy'})

# CORS test endpoint
@combined_app.route('/api/cors-test')
def cors_test():
    return jsonify({
        'message': 'CORS is working correctly',
        'origin': request.headers.get('Origin', 'Unknown')
    })

# Serve the React app
@combined_app.route('/', defaults={'path': ''})
@combined_app.route('/<path:path>')
def serve(path):
    # If the path is for an API endpoint, let the API handle it
    if path.startswith('api/'):
        # This will be handled by the routes above
        pass

    # Check if the requested file exists in the static folder
    if path and os.path.exists(os.path.join(combined_app.static_folder, path)):
        return send_from_directory(combined_app.static_folder, path)

    # Otherwise, serve the index.html file for client-side routing
    return send_from_directory(combined_app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    combined_app.run(host='0.0.0.0', port=port)
