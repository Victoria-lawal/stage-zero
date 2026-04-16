Stage 0: API Integration & Data Processing

Overview

This project implements a single GET endpoint that integrates with the Genderize API, processes the response, and returns a structured result.

Live Endpoint
GET /api/classify?name={name}

Example:

/api/classify?name=victoria

Success Response (200 OK)
{
  "status": "success",
  "data": {
    "name": "victoria",
    "gender": "female",
    "probability": 0.99,
    "sample_size": 479603,
    "is_confident": true,
    "processed_at": "2026-04-16T08:19:05Z"
  }
}
Error Responses
400 — Missing or empty name
{
  "status": "error",
  "message": "Missing name parameter"
}
422 — Invalid name type
{
  "status": "error",
  "message": "name must be a string"
}
502 — External API failure
{
  "status": "error",
  "message": "External API failure"
}
No prediction available
{
  "status": "error",
  "message": "No prediction available for the provided name"
}

Processing Logic
Extract gender, probability, and count
Rename count → sample_size
Compute:
is_confident = true if:
probability ≥ 0.7
sample_size ≥ 100
Generate processed_at dynamically in UTC (ISO 8601 format)

Tech Stack
Python
FastAPI
HTTPX

Running Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

Visit:

http://127.0.0.1:8000/api/classify?name=john

Deployment

Deployed on Railway 
--link goes here
Testing

Tested using:

Browser (localhost and deployed endpoint)

Notes
CORS enabled (Access-Control-Allow-Origin: *)
Handles edge cases from Genderize API
Response time optimized (<500ms excluding API latency)