# Docker Deployment Guide for Alumni Management System

This guide explains how to deploy the Alumni Management System using Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your system

## Deployment Steps

### 1. Clone the Repository

If you haven't already, clone the repository to your local machine.

### 2. Navigate to the Project Directory

```bash
cd AlumniManagementSystem
```

### 3. Deploy the Application

Run the deployment script:

```bash
# On Windows
deploy.bat

# On Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

Alternatively, you can manually run:

```bash
docker-compose up -d --build
```

This command will:
- Build the Docker images for both the client and server
- Start the containers in detached mode

### 4. Access the Application

Once the deployment is complete, you can access the application at:

- Frontend: http://localhost
- Backend API: http://localhost:5000

### 5. Default Login Credentials

Use the following credentials to log in:

- Email: admin@alumni.edu
- Password: admin123

### 6. Stop the Application

To stop the application, run:

```bash
# On Windows
stop.bat

# On Linux/Mac
chmod +x stop.sh
./stop.sh
```

Alternatively, you can manually run:

```bash
docker-compose down
```

## Docker Architecture

The application is containerized using Docker with the following components:

1. **Server Container (alumni-server)**
   - Python Flask backend
   - Connects to MongoDB Atlas
   - Exposes port 5000

2. **Client Container (alumni-client)**
   - React frontend
   - Nginx web server
   - Exposes port 80
   - Proxies API requests to the server container

## Troubleshooting

### Container Logs

To view logs for a specific container:

```bash
# View server logs
docker logs alumni-server

# View client logs
docker logs alumni-client
```

### Restarting Containers

If you need to restart the containers:

```bash
docker-compose restart
```

### Rebuilding Containers

If you've made changes to the code and need to rebuild:

```bash
docker-compose up -d --build
```

## Environment Variables

The following environment variables are used:

- `MONGODB_URI`: MongoDB connection string
- `DATABASE_NAME`: MongoDB database name
- `JWT_SECRET_KEY`: Secret key for JWT token generation

These are configured in the `docker-compose.yml` file.

## Data Persistence

The MongoDB data is stored in MongoDB Atlas, so it persists even if the containers are removed.

## Security Notes

- The MongoDB connection string is included in the Docker Compose file. In a production environment, consider using Docker secrets or environment variables.
- The JWT secret key should be changed in a production environment.
- HTTPS is not configured in this setup. For production, consider adding HTTPS support.
