# Book_library_RestAPI
# Book Library REST API

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

A robust, scalable REST API for managing a digital book library with JWT-based authentication, role-based access control, and comprehensive CRUD operations.

## 🚀 Features

- **🔐 JWT Authentication**: Secure token-based authentication system
- **👥 Role-Based Access Control**: Admin and User role segregation
- **📚 Complete CRUD Operations**: Full book management capabilities
- **🛡️ Security First**: Password hashing and secure token validation
- **📱 RESTful Design**: Industry-standard REST API principles
- **🔍 Comprehensive Logging**: Detailed request/response logging
- **📊 Error Handling**: Structured error responses with proper HTTP status codes
- **🚀 Production Ready**: Optimized for deployment and scaling

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [API Documentation](#api-documentation)
5. [Authentication](#authentication)
6. [Error Handling](#error-handling)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

## 🏃‍♂️ Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/book-library-api.git
cd book-library-api

# Install dependencies
pip install -r requirements.txt

# Run the application
python bookapp.py

# API will be available at http://localhost:5000
```

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Dependencies

```bash
pip install flask==2.3.3
pip install PyJWT==2.8.0
pip install Werkzeug==2.3.7
pip install requests==2.31.0
```

### Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/book-library-api.git
   cd book-library-api
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
DATABASE_URL=sqlite:///books.db
JWT_EXPIRATION_HOURS=24
```

### Production Configuration

For production deployment, ensure:

- Use a cryptographically secure `SECRET_KEY`
- Set `FLASK_DEBUG=False`
- Configure proper database connection
- Enable HTTPS
- Set up proper logging

## 📖 API Documentation

### Base URL
```
http://localhost:5000
```

### Authentication Header
```
Authorization: Bearer <your-jwt-token>
```

## 🔐 Authentication

### Register User
```http
POST /register
Content-Type: application/json

{
    "username": "string",
    "password": "string",
    "role": "admin|user"  // optional, defaults to "user"
}
```

**Response:**
```json
{
    "message": "User admin registered successfully!"
}
```

### Login
```http
POST /login
Content-Type: application/json

{
    "username": "string",
    "password": "string"
}
```

**Response:**
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## 📚 Book Management

### Get All Books
```http
GET /books
```

**Response:**
```json
[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    }
]
```

### Get Book by ID
```http
GET /books/{id}
```

**Response:**
```json
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```

### Add New Book (Admin Only)
```http
POST /books
Authorization: Bearer <admin-token>
Content-Type: application/json

{
    "title": "string",
    "author": "string"
}
```

**Response:**
```json
{
    "id": 3,
    "title": "1984",
    "author": "George Orwell"
}
```

### Update Book (Admin Only)
```http
PUT /books/{id}
Authorization: Bearer <admin-token>
Content-Type: application/json

{
    "title": "string",      // optional
    "author": "string"      // optional
}
```

**Response:**
```json
{
    "id": 1,
    "title": "The Great Gatsby - Updated",
    "author": "F. Scott Fitzgerald"
}
```

### Delete Book (Admin Only)
```http
DELETE /books/{id}
Authorization: Bearer <admin-token>
```

**Response:**
```json
{
    "message": "Book deleted"
}
```

## 🚨 Error Handling

### Error Response Format
```json
{
    "message": "Error description",
    "error_code": "SPECIFIC_ERROR_CODE",
    "timestamp": "2024-01-15T10:30:00Z"
}
```

### HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid request data |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 409 | Conflict - Resource already exists |
| 500 | Internal Server Error - Server error |

### Common Error Scenarios

**Authentication Errors:**
```json
{
    "message": "Token is missing!",
    "error_code": "AUTH_TOKEN_MISSING"
}
```

**Permission Errors:**
```json
{
    "message": "Admin privilege required",
    "error_code": "INSUFFICIENT_PERMISSIONS"
}
```

**Validation Errors:**
```json
{
    "message": "Title and author required",
    "error_code": "VALIDATION_ERROR"
}
```

## 🧪 Testing

### Automated Testing

Run the comprehensive test suite:

```bash
python test_api.py
```

### Manual Testing with cURL

**Register a new admin user:**
```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123", "role": "admin"}'
```

**Login and get token:**
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Add a book:**
```bash
curl -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"title": "1984", "author": "George Orwell"}'
```

### Postman Collection

Import the provided Postman collection (`book-library-api.postman_collection.json`) for comprehensive API testing.

## 🚀 Deployment

### Local Development
```bash
python bookapp.py
```

### Production Deployment

#### Using Gunicorn (Recommended)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 bookapp:app
```

#### Using Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "bookapp:app"]
```

#### Environment-Specific Configurations

**Development:**
- Debug mode enabled
- Detailed error messages
- Auto-reload on code changes

**Production:**
- Debug mode disabled
- Error logging to files
- Performance optimizations
- Security headers

### Security Considerations

1. **Use HTTPS in production**
2. **Set strong SECRET_KEY**
3. **Implement rate limiting**
4. **Use environment variables for sensitive data**
5. **Regular security audits**
6. **Input validation and sanitization**

## 📊 Performance & Monitoring

### Metrics to Monitor

- Response time per endpoint
- Request volume
- Error rates
- Authentication failures
- Database query performance

### Recommended Tools

- **APM**: New Relic, DataDog
- **Logging**: ELK Stack, Splunk
- **Monitoring**: Prometheus + Grafana

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 coding standards
- Write comprehensive tests
- Update documentation
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🆘 Support

### Getting Help

- **Documentation**: Check this README first
- **Issues**: [GitHub Issues](https://github.com/yourusername/book-library-api/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/book-library-api/discussions)

### FAQ

**Q: How do I reset a forgotten password?**
A: Currently, password reset functionality is not implemented. Contact admin for manual reset.

**Q: Can I use this API with a frontend application?**
A: Yes! Enable CORS by installing `flask-cors` and adding CORS headers.

**Q: Is there a rate limit?**
A: No built-in rate limiting. Implement using `flask-limiter` for production use.

## 🔄 Changelog

### Version 1.0.0 (2024-01-15)
- Initial release
- JWT authentication
- CRUD operations for books
- Role-based access control

---

**Built with ❤️ using Flask and Python**

*For enterprise support and custom development, contact: [your-email@domain.com]*
