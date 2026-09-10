# System Design & Architecture - Cars24 Assignment

## Architecture Overview
1. **Client Request:** The user sends a POST request with a natural language query string (e.g., "Find all diesel cars").
2. **LLM Translation Layer:** The backend injects the SQLite database schema into a structured prompt and sends it to the `gemini-3.6-flash` model to dynamically generate a secure `SELECT` statement.
3. **Execution & Safeguards:** The system validates that the query begins with `SELECT` to prevent destructive operations, then safely executes it against the local SQLite database.
4. **Response Payload:** Matching vehicle rows are serialized into JSON and returned to the client.

## Technical Choices & Trade-offs
- **FastAPI:** Chosen for its lightning-fast performance, automatic data validation via Pydantic, and built-in interactive Swagger UI (`/docs`).
- **SQLite:** Keeps the assignment entirely self-contained and portable without requiring external database containers or complex setup steps.
- **Gemini AI:** Provides robust natural language understanding, seamlessly parsing complex constraints (price ranges, fuel types, mileage).
