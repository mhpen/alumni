const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();

// Enable CORS for all routes
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// Parse JSON request bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Create a proxy for the API
const apiProxy = createProxyMiddleware({
  target: 'https://alumni-server-1-zato.onrender.com',
  changeOrigin: true,
  secure: false, // Don't verify SSL certificates
  timeout: 60000, // Increase timeout to 60 seconds
  proxyTimeout: 60000, // Increase proxy timeout to 60 seconds
  followRedirects: true, // Follow redirects
  pathRewrite: function(path, req) {
    // Log the original path
    console.log(`Original path: ${path}`);

    // Keep the path as is - no rewriting needed
    const newPath = path;
    console.log(`Rewritten path: ${newPath}`);
    return newPath;
  },
  logLevel: 'debug', // Add debug logging
  onProxyReq: function(proxyReq, req, res) {
    // Log the request
    console.log(`Proxying ${req.method} request to: ${proxyReq.path}`);
    console.log(`Original URL: ${req.originalUrl}`);
    console.log(`Base URL: ${req.baseUrl}`);
    console.log(`Path: ${req.path}`);

    // If it's a POST request, log the body
    if (req.method === 'POST' && req.body) {
      console.log('Request body:', req.body);
    }
  },
  onProxyRes: function(proxyRes, req, res) {
    // Add CORS headers to the response
    proxyRes.headers['Access-Control-Allow-Origin'] = '*';
    proxyRes.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS';
    proxyRes.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization';

    // Log the response status
    console.log(`Response status: ${proxyRes.statusCode}`);

    // If it's an error, log more details
    if (proxyRes.statusCode >= 400) {
      console.error(`Error response for ${req.method} ${req.originalUrl}`);
      console.error(`Status: ${proxyRes.statusCode}`);
      console.error(`Headers:`, proxyRes.headers);
    }
  },

  // Handle proxy errors
  onError: function(err, req, res) {
    console.error('Proxy error:', err);

    // Send a response to the client
    if (!res.headersSent) {
      res.writeHead(500, {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
      });

      // Create a user-friendly error message
      const errorMessage = {
        error: 'Proxy Error',
        message: 'The server is currently unavailable. Please try again later.',
        details: err.message
      };

      res.end(JSON.stringify(errorMessage));
    }
  }
});

// Use the proxy for all /api routes
app.use('/api', apiProxy);

// Add a health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'healthy' });
});

// Add a test endpoint
app.post('/test-login', (req, res) => {
  console.log('Test login request received');
  console.log('Request body:', req.body);

  // Check if the credentials are correct
  const { email, password } = req.body;
  if (email === 'admin@alumni.edu' && password === 'admin123') {
    // Return a success response
    res.json({
      message: 'Login successful',
      token: 'test_token',
      user: {
        id: '1',
        name: 'Admin User',
        email: email
      }
    });
  } else {
    // Return an error response
    res.status(401).json({
      message: 'Invalid email or password'
    });
  }
});

// Start the server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Proxy server running on port ${PORT}`);
  console.log(`Proxying requests to https://alumni-server-1-zato.onrender.com`);
});
