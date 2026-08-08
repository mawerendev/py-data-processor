# Python Data Processor & Analytics API (`py-data-processor`)

A modular Python REST API designed to process text metrics and safely store reports using both file-based JSON output and an embedded SQLite relational database. Built following industry best practices, clean architecture, and automated test coverage.

---

## Key Features

* **Text Metrics Extraction:** Calculates character counts, word counts, and identifies the longest word in a given text payload.
* **REST API Endpoints:** Powered by FastAPI with validation via Pydantic schemas.
* **Dual Persistence Layer:**
  * **JSON Exporter:** Generates formatted JSON file reports with isolated directory management.
  * **SQLite Database Engine:** Inserts and retrieves metric records using parameterized SQL queries to prevent SQL injection.
* **Automated Unit Testing:** Includes high-coverage test suites built with `pytest`, utilizing in-memory SQLite databases (`:memory:`) and FastAPI `TestClient` for isolated testing.
* **Clean Architecture:** Strict separation of concerns between business logic (`src/`), API routes (`main.py`), and test suites (`tests/`).

---

## Project Structure

```text
py-data-processor/
├── src/
│   ├── __init__.py
│   ├── data_processor.py   # Text analysis logic & JSON generation
│   └── db_manager.py       # SQLite connection manager & CRUD queries
├── tests/
│   ├── test_api.py         # Integration tests for FastAPI endpoints
│   └── test_db_manager.py # In-memory unit tests for SQL operations
├── main.py                 # FastAPI application & entry point
├── requirements.txt        # Environment dependencies
├── .gitignore              # Ignored files (DBs, caches, venv)
└── README.md               # Project documentation
Quick Start
1. Environment Setup
PowerShell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
2. Run the API Server
PowerShell
uvicorn main:app --reload
Access the interactive API documentation at http://127.0.0.1:8000/docs.

3. Run Test Suite
PowerShell
python -m pytest
Author
mawerendev - GitHub Profile
