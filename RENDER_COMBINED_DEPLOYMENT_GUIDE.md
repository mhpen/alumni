# Deploying Combined Alumni Management System on Render.com

This guide explains how to deploy the combined Docker image of the Alumni Management System on Render.com.

## Prerequisites

- Docker Hub account (username: ynodev)
- Render.com account
- Combined Docker image pushed to Docker Hub (`ynodev/alumni-combined:latest`)

## Deployment Options

### Option 1: Deploy Using Render Dashboard (Manual)

1. **Log in to your Render.com dashboard**
   - Go to [dashboard.render.com](https://dashboard.render.com)

2. **Create a new Web Service**
   - Click on "New" and select "Web Service"
   - Choose "Deploy an existing image from a registry"

3. **Configure the service**
   - **Name**: `alumni-management-system`
   - **Image URL**: `docker.io/ynodev/alumni-combined:latest`
   - **Region**: Choose the region closest to your users
   - **Instance Type**: Start with "Starter" plan (or choose based on your needs)

4. **Set the environment variables**
   - Copy all environment variables from the `render-combined-env.yaml` file
   - Add them to the "Environment" section in the Render dashboard

5. **Configure the port**
   - Set the port to `5000` (this is the port your application listens on inside the container)

6. **Create the Web Service**
   - Click "Create Web Service"

### Option 2: Deploy Using Render Blueprint (Automated)

1. **Create a new repository or use your existing one**
   - Make sure it contains your `render-combined-env.yaml` file

2. **Deploy using the Blueprint**
   - Log in to your Render dashboard
   - Click on "New" and select "Blueprint"
   - Connect your GitHub account if you haven't already
   - Select the repository containing your `render-combined-env.yaml` file
   - Click "Apply Blueprint"

3. **Verify the deployment**
   - Render will automatically deploy your service with all the specified environment variables

### Option 3: Deploy Using Render CLI

1. **Install the Render CLI**
   ```bash
   npm install -g @render/cli
   ```

2. **Log in to Render**
   ```bash
   render login
   ```

3. **Deploy using the YAML file**
   ```bash
   render blueprint apply --file render-combined-env.yaml
   ```

## Accessing Your Application

Once the deployment is complete, you can access your application at the URL provided by Render (e.g., `https://alumni-management-system.onrender.com`).

Use the default login credentials:
- Email: admin@alumni.edu
- Password: admin123

## Environment Variables Explanation

The `render-combined-env.yaml` file contains all the necessary environment variables for your application:

### Database Configuration
- `MONGODB_URI`: Connection string for MongoDB Atlas
- `DATABASE_NAME`: Name of the MongoDB database

### Security Configuration
- `JWT_SECRET_KEY`: Secret key for JWT token generation
- `JWT_ACCESS_TOKEN_EXPIRES`: Token expiration time in seconds

### Server Configuration
- `PORT`: Port the application listens on (5000)
- `HOST`: Host to bind to (0.0.0.0 allows external connections)
- `DEBUG`: Whether to run in debug mode

### CORS Configuration
- `CORS_ALLOW_ORIGINS`: Origins allowed to make cross-origin requests

### Application Configuration
- `APP_NAME`: Name of the application
- `ADMIN_EMAIL`: Default admin email
- `ADMIN_PASSWORD`: Default admin password

### Model Configuration
- `MODEL_STORAGE_TYPE`: Where to store ML models (mongodb or filesystem)
- `MODEL_COLLECTION_PREFIX`: Prefix for model collections in MongoDB

### Logging Configuration
- `LOG_LEVEL`: Level of logging detail

### Performance Configuration
- `GUNICORN_WORKERS`: Number of worker processes
- `GUNICORN_THREADS`: Number of threads per worker
- `GUNICORN_TIMEOUT`: Request timeout in seconds

### Feature Flags
- `ENABLE_MODEL_TRAINING`: Whether to enable model training
- `ENABLE_ANALYTICS`: Whether to enable analytics features
- `ENABLE_SAMPLE_GENERATION`: Whether to enable sample data generation

### Render-specific Configuration
- `RENDER_EXTERNAL_URL`: The public URL of your service

### Email Configuration (Optional)
- SMTP settings for sending emails (if implemented)

## Updating Your Deployment

When you push a new version of your Docker image to Docker Hub:

1. Go to your service in the Render dashboard
2. Click on "Manual Deploy" > "Deploy latest image"

## Monitoring and Logs

1. Go to your service in the Render dashboard
2. Click on "Logs" to view application logs
3. Set up alerts for important events

## Scaling Your Application

As your user base grows, you can scale your application:

1. Go to your service in the Render dashboard
2. Click on "Settings"
3. Upgrade your plan or adjust the number of instances

## Troubleshooting

### Issue: Application Not Starting

Check the logs in the Render dashboard for any startup errors. Common issues include:

- Incorrect MongoDB URI
- Missing environment variables
- Port conflicts

### Issue: Database Connection Problems

If you encounter database connection issues:

1. Verify that the MongoDB URI is correct
2. Check if the MongoDB Atlas IP whitelist allows connections from Render.com
3. Check the logs in the Render dashboard for any connection errors

### Issue: Authentication Problems

If users cannot log in:

1. Check that the JWT_SECRET_KEY is set correctly
2. Verify that the default admin credentials are working
3. Check for any errors in the authentication process in the logs

## Security Recommendations

For production deployments:

1. Change the default admin password
2. Use a strong, unique JWT secret key
3. Consider restricting CORS to specific origins
4. Enable HTTPS (Render provides this by default)
5. Store sensitive environment variables as secrets in Render

## Backup and Recovery

1. Regularly backup your MongoDB database
2. Document your environment configuration
3. Consider setting up automated backups

## Support and Resources

- [Render Documentation](https://render.com/docs)
- [Docker Documentation](https://docs.docker.com)
- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com)
