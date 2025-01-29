# FastAPI Stage Zero API

## Project Description
This is a simple FastAPI application that provides an endpoint to retrieve basic informations. The API returns a JSON response containing an email, the current datetime in UTC (ISO 8601 format), and a GitHub repository link.

Additionally, the application is configured with Cross-Origin Resource Sharing (CORS) to allow requests from any origin.

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- FastAPI (pip install fastapi[standard], runs the trick)
- Uvicorn

### Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/Egcarson/hng12-stage-zero.git
   cd hng12-stage-zero
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**
   ```sh
   fastapi dev main.py
   ```

The API will be accessible at: `http://127.0.0.1:8000/stage-zero`

## API Documentation
### **Endpoint: GET /stage-zero**
**Description:** Returns a JSON object containing the email, current UTC datetime, and GitHub repository URL.

**URL:**
```
GET /stage-zero
```

**Response Format:**
```json
{
    "email": "esehgodprevail@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/Egcarson/hng12-stage-zero.git"
}
```

### Example Usage
You can test the API live:
- [Swagger Documentation](https://hng12-stage-zero.onrender.com/)
- [Direct Request](https://hng12-stage-zero.onrender.com/stage-zero)

Or with Python:
```python
import requests

response = requests.get("http://127.0.0.1:8000/stage-zero")
print(response.json())
```

## Useful Links
- [Hire Python Developers](https://hng.tech/hire/python-developers)
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Golang Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)

