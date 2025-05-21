# Deploying Alumni Management System on Render.com

This guide explains how to deploy the Alumni Management System on Render.com using the source code directly from GitHub.

## Option 1: Deploy Using Render Blueprint (Recommended)

The easiest way to deploy the Alumni Management System on Render.com is to use the Render Blueprint (render.yaml file) we've created.

### Step 1: Fork the Repository to Your GitHub Account

1. Go to the GitHub repository containing the Alumni Management System
2. Click on "Fork" to create a copy in your GitHub account

### Step 2: Deploy Using Render Blueprint

1. Log in to your [Render.com](https://dashboard.render.com/) account
2. Click on "New" and select "Blueprint"
3. Connect your GitHub account if you haven't already
4. Select the forked repository
5. Click "Apply Blueprint"

Render will automatically:
- Deploy the backend API service
- Deploy the frontend service
- Configure the environment variables
- Set up the connection between the services

### Step 3: Access Your Application

Once the deployment is complete, you can access your application at the URL provided by Render for the frontend service.

Use the default login credentials:
- Email: admin@alumni.edu
- Password: admin123

## Option 2: Deploy Using Docker Images

If you prefer to deploy using pre-built Docker images:

### Step 1: Create a Web Service on Render for the Backend

1. Log in to your Render dashboard
2. Click on "New" and select "Web Service"
3. Choose "Deploy an existing image from a registry"
4. Enter the following details:
   - **Name**: `alumni-management-server`
   - **Image URL**: `docker.io/ynodev/alumni-server:latest`
   - **Region**: Choose the region closest to your users
   - **Instance Type**: Start with "Starter" plan
   - **Environment Variables**:
     - `MONGODB_URI`: `mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement`
     - `DATABASE_NAME`: `alumni_management`
     - `JWT_SECRET_KEY`: `your_super_secret_key_for_jwt_tokens`
     - `CORS_ORIGIN`: (Leave blank for now, we'll update this after creating the frontend service)
   - **Port**: `5000`
5. Click "Create Web Service"

### Step 2: Create a Web Service on Render for the Frontend

1. In your Render dashboard, click on "New" and select "Web Service" again
2. Choose "Deploy an existing image from a registry"
3. Enter the following details:
   - **Name**: `alumni-management-client`
   - **Image URL**: `docker.io/ynodev/alumni-client:latest`
   - **Region**: Choose the same region as your backend service
   - **Instance Type**: Start with "Starter" plan
   - **Environment Variables**:
     - `API_URL`: (The URL of your backend service, e.g., `https://alumni-management-server.onrender.com`)
   - **Port**: `80`
4. Click "Create Web Service"

### Step 3: Update CORS Settings

After both services are deployed:

1. Go to your backend service in the Render dashboard
2. Click on "Environment"
3. Add or update the `CORS_ORIGIN` environment variable with the URL of your frontend service
4. Click "Save Changes"

## Troubleshooting

### Issue: "No module named 'pandas'"

If you encounter this error:

```
ModuleNotFoundError: No module named 'pandas'
```

This means the required Python packages are missing from your Docker image. We've already fixed this by updating the `requirements.txt` file to include pandas and other required packages.

### Issue: Connection Problems Between Frontend and Backend

If the frontend can't connect to the backend:

1. Check that the API URL environment variable is set correctly
2. Verify that CORS is properly configured on the backend
3. Check the network requests in your browser's developer tools for any errors

### Issue: Database Connection Problems

If you encounter database connection issues:

1. Verify that the MongoDB URI is correct
2. Check if the MongoDB Atlas IP whitelist allows connections from Render.com
3. Check the logs in the Render dashboard for any connection errors

## Monitoring Your Application

Render provides built-in monitoring and logging:

1. Go to your service in the Render dashboard
2. Click on "Logs" to view application logs
3. Set up alerts for important events

## Scaling Your Application

As your user base grows, you can scale your application:

1. Go to your service in the Render dashboard
2. Click on "Settings"
3. Upgrade your plan or adjust the number of instances

## Option 3: Automated Deployment with GitHub Actions

For a fully automated deployment workflow:

### Step 1: Set Up GitHub Repository

1. Push your code to a GitHub repository
2. Add the render.yaml file to the root of your repository

### Step 2: Configure GitHub Actions

1. Create a `.github/workflows/render-deploy.yml` file in your repository (we've already created this for you)
2. Get your Render API key from the Render dashboard (Account Settings > API Keys)
3. Add the following secrets to your GitHub repository:
   - `RENDER_API_KEY`: Your Render API key
   - `RENDER_SERVICE_ID`: The ID of your Render service (found in the URL of your service page)

### Step 3: Trigger Deployments

Now, whenever you push to the main branch of your repository, GitHub Actions will automatically deploy your application to Render.

## Updating Your Application

### Option 1: With GitHub Actions

If you've set up GitHub Actions:

1. Make changes to your code
2. Commit and push to the main branch
3. GitHub Actions will automatically deploy the changes to Render

### Option 2: Manual Update

If you're using Docker images:

1. Push a new version of your Docker image to Docker Hub
2. Go to your service in the Render dashboard
3. Click on "Manual Deploy" > "Deploy latest image"

### Option 3: Using Render Dashboard

If you're deploying directly from GitHub:

1. Make changes to your code
2. Commit and push to your repository
3. Render will automatically detect the changes and deploy them (if auto-deploy is enabled)
4. Alternatively, go to your service in the Render dashboard and click "Manual Deploy"
