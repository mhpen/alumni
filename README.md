# Alumni Management System

A comprehensive system for managing alumni data, tracking career paths, and predicting employment probabilities using machine learning.

## Features

- **Admin Dashboard**: Modern UI for administrators to manage alumni data
- **Career Path Prediction**: ML model to predict career paths based on degree and skills
- **Employment Probability**: ML model to predict employment probability post-graduation
- **Data Visualization**: Interactive charts and graphs for analytics
- **MongoDB Integration**: Secure storage of alumni data and ML models
- **Combined Deployment**: Frontend and backend served from a single application

## Getting Started

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB instance)
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. Clone the repository or download the source code
2. Ensure you have Python installed
3. Run the start script:

```
start_alumni_system.bat
```

This will:
- Set up a Python virtual environment
- Install all required dependencies
- Initialize the database with sample data
- Start the server
- Open the client in your default browser

### Deployment

This application is configured for deployment on Render.com using the combined deployment approach, which serves both the frontend and backend from a single server.

For detailed deployment instructions, see [README-COMBINED-DEPLOY.md](README-COMBINED-DEPLOY.md).

## Usage

### Admin Login

- **URL**: http://localhost:5000
- **Default Credentials**:
  - Email: admin@alumni.edu
  - Password: admin123

### Dashboard

The dashboard provides an overview of key metrics:
- Total alumni count
- Employment rate
- Graduation rate
- Average salary
- Recent activity

### Machine Learning Models

The system includes two ML models:
1. **Career Path Prediction**: Predicts potential career paths based on degree and skills
2. **Employment Probability**: Predicts the likelihood of employment after graduation

## Project Structure

```
AlumniManagementSystem/
├── client/                  # Frontend code
│   ├── assets/              # CSS, JS, and images
│   ├── index.html           # Login page
│   └── dashboard.html       # Admin dashboard
├── server/                  # Backend code
│   ├── src/                 # Source code
│   │   ├── models/          # Data models
│   │   ├── routes/          # API routes
│   │   └── app.py           # Flask application
│   ├── init_db.py           # Database initialization
│   ├── run.py               # Server entry point
│   └── requirements.txt     # Python dependencies
├── dataset/                 # ML datasets
├── start_alumni_system.bat  # Startup script
└── README.md                # This file
```

## API Endpoints

- `/api/admin/login` - Admin login
- `/api/admin/dashboard` - Dashboard data
- `/api/admin/profile` - Admin profile

## Technologies Used

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Flask (Python)
- **Database**: MongoDB
- **ML**: Scikit-learn, XGBoost, Random Forest
- **Authentication**: JWT
- **Deployment**: Render.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed by Augment Agent
- Powered by Alumni Management System
