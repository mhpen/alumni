from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Check if we're running in the combined Docker image
STATIC_FOLDER = '/app/static' if os.path.exists('/app/static') else None

# Create Flask app with explicit static_url_path
app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='/static')
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_super_secret_key_for_jwt_tokens')
jwt = JWTManager(app)

# Configure MongoDB
mongodb_uri = os.getenv('MONGODB_URI', 'mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement')
database_name = os.getenv('DATABASE_NAME', 'alumni_management')
client = MongoClient(mongodb_uri)
db = client[database_name]
app.config['DATABASE'] = db

# Import routes
from .routes.admin_routes import admin_bp
from .routes.analytics_routes import analytics_bp
from .routes.prediction_routes import prediction_bp

# Register blueprints
app.register_blueprint(admin_bp, url_prefix='/api')
app.register_blueprint(analytics_bp, url_prefix='/api')
app.register_blueprint(prediction_bp, url_prefix='/api')

# Explicitly serve static files with correct content type
@app.route('/static/<path:filename>')
def serve_static(filename):
    response = send_from_directory(app.static_folder, filename)
    if filename.endswith('.js'):
        response.headers['Content-Type'] = 'application/javascript'
    elif filename.endswith('.css'):
        response.headers['Content-Type'] = 'text/css'
    return response

# Serve the React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    # First check if the path is an API route
    if path.startswith('api/'):
        return app.view_functions['api.index']()
    
    # Then check if it's a static file
    if path.startswith('static/'):
        return serve_static(path[7:])  # Remove 'static/' prefix
    
    # Check if the file exists in the static folder
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Otherwise serve the index.html
    return send_from_directory(app.static_folder, 'index.html')

# API home route
@app.route('/api')
def api_home():
    return jsonify({'message': 'Alumni Management System API'})

# Health check endpoint
@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy'})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    if request.path.startswith('/api/'):
        return jsonify({'message': 'API resource not found'}), 404
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(500)
def server_error(error):
    return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
