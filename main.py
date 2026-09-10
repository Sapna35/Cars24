import os
import sqlite3
from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel

app = FastAPI()

# Initialize the Gemini client (it will automatically look for the GEMINI_API_KEY environment variable)
# Alternatively, you can pass your key directly: client = genai.Client(api_key="your-key-here")
client = genai.Client()


class SearchRequest(BaseModel):
  query: str


def get_db_schema():
  conn = sqlite3.connect("cars.db")
  cursor = conn.cursor()
  cursor.execute(
      "SELECT name FROM sqlite_master WHERE type='table' AND name='vehicles';"
  )
  schema = """
    Table: vehicles
    Columns:
    - id (INTEGER)
    - brand (TEXT)
    - model (TEXT)
    - price (INTEGER)
    - fuel_type (TEXT)
    - kilometers (INTEGER)
    """
  conn.close()
  return schema


@app.post("/search")
def search_vehicles(request: SearchRequest):
  schema = get_db_schema()

  # Prompt engineering: Instruct Gemini to act as a Text-to-SQL translator
  prompt = f"""
    You are a backend assistant. Given the following SQLite database schema:
    {schema}

    Convert this natural language search request into a valid SQL SELECT query for the 'vehicles' table.
    Make sure to handle text matching case-insensitively (for example, use LOWER(fuel_type) = LOWER('value') or LIKE).
    Return ONLY the raw SQL query string, nothing else. Do not use markdown blocks like ```sql.

    Request: "{request.query}"
    """

  try:
    # Call Gemini to generate the SQL query
    response = client.models.generate_content(
        model="gemini-3.6-flash", contents=prompt
    )
    sql_query = response.text.strip()

    # Safety check: ensure it's a SELECT query
    if not sql_query.upper().startswith("SELECT"):
      raise HTTPException(
          status_code=400,
          detail="AI generated an invalid query structure.",
      )

    # Execute query on sqlite database
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    conn.close()

    return {
        "user_query": request.query,
        "generated_sql": sql_query,
        "results": rows,
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))