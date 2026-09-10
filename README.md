# Cars24 AI Vehicle Search Engine 🚗

A natural language backend service built with FastAPI, SQLite, and Google Gemini AI, allowing users to search a vehicle catalog using everyday conversational queries.

## Features
- **Natural Language to SQL:** Powered by Gemini 3.6 Flash to translate free-form text into secure database queries.
- **Robust REST API:** Built with FastAPI for high performance and automatic interactive documentation.
- **Automated Seed Data:** Includes a script to generate a rich, realistic vehicle dataset.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sapna35/Cars24.git](https://github.com/Sapna35/Cars24.git)
   cd Cars24

   Install dependencies:
   ```bash
   pip install fastapi uvicorn openai sqlalchemy google-genai

   Set your Gemini API key:
   ```bash
   $env:GEMINI_API_KEY="your_api_key"

   Generate the database seed data:
   ```bash
   python seed.py

   Run the application:
   ```bash
   uvicorn main:app --reload

   Open your browser and navigate to:
http://127.0.0.1:8000/docs

API Endpoints
Search Vehicles
URL: /search

Method: POST

Content-Type: application/json

Request Body Example:
 ```bash
 {
  "query": "Find all diesel cars"
}

 ```bash
 {
  "user_query": "Find all diesel cars",
  "generated_sql": "SELECT * FROM vehicles WHERE LOWER(fuel_type) = 'diesel';",
  "results": [
    [1, "Hyundai", "Creta", 1400000, "Diesel", 45000],
    [3, "Tata", "Nexon", 1200000, "Diesel", 30000]
  ]
}
