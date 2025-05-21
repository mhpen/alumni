import sys
import os

# Add the current directory to the path so we can import the src package
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.app import app
from create_default_admin import create_default_admin

if __name__ == "__main__":
    # Create default admin user if it doesn't exist
    create_default_admin()

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
