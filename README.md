# Alumni Management System

A comprehensive system for managing alumni data, tracking career paths, and predicting employment probabilities using machine learning.

## Features

- **Admin Dashboard**: Modern UI for administrators to manage alumni data
- **Career Path Prediction**: ML model to predict career paths based on degree and skills
- **Employment Probability**: ML model to predict employment probability post-graduation
- **Data Visualization**: Interactive charts and graphs for analytics
- **MongoDB Integration**: Secure storage of alumni data and ML models

## Getting Started

### Prerequisites

- Docker and Docker Compose (for containerized deployment)
- MongoDB Atlas account (or local MongoDB instance)
- Modern web browser (Chrome, Firefox, Edge)
- Git (for version control)

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/ynodev/alumni.git
   cd alumni
   ```

2. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values as needed

3. Run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

4. Access the application at http://localhost:5000

### Production Deployment

#### Using Docker

1. Build the Docker image:
   ```
   docker build -t alumni-management-system .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 --env-file .env alumni-management-system
   ```

#### Using Blueprint

1. Deploy using the blueprint.yaml configuration:
   ```
   # Using your preferred container platform
   # Example for Kubernetes:
   kubectl apply -f blueprint.yaml
   ```

#### Manual Deployment

If you prefer to run the application without Docker:

1. Install Python 3.8+ and Node.js 18+
2. Set up the server:
   ```
   cd server
   pip install -r requirements.txt
   npm install
   ```

3. Set up the client:
   ```
   cd client
   npm install
   npm run build
   ```

4. Start the combined application:
   ```
   cd server
   python combined_app.py
   ```

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
├── client/                  # Frontend React application
│   ├── build/               # Production build
│   ├── public/              # Public assets
│   ├── src/                 # React source code
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   └── App.js           # Main application component
│   ├── package.json         # Node.js dependencies
│   └── tailwind.config.js   # Tailwind CSS configuration
├── server/                  # Backend Flask application
│   ├── src/                 # Source code
│   │   ├── models/          # Data models
│   │   ├── routes/          # API routes
│   │   └── utils/           # Utility functions
│   ├── combined_app.py      # Combined Flask application
│   ├── init_db.py           # Database initialization
│   ├── run.py               # Server entry point
│   └── requirements.txt     # Python dependencies
├── models/                  # ML model files
├── employment_models/       # Employment prediction models
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── blueprint.yaml           # Blueprint deployment configuration
├── .env.example             # Example environment variables
├── start_alumni_system.bat  # Local startup script
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed by Augment Agent
- Powered by Alumni Management System
