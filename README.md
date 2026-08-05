Markdown
# Python Data Processor & Analytics Engine (`py-data-processor`)

A modular Python application designed to process text metrics and safely store reports using both file-based JSON output and an embedded SQLite relational database. Built following industry best practices, clean architecture, and automated test coverage.

---

## Key Features

* **Text Metrics Extraction:** Calculates character counts, total words, and identifies the longest word in a given text payload.
* **Dual Persistence Layer:**
  * **JSON Exporter:** Generates formatted JSON file reports with isolated directory management.
  * **SQLite Database Engine:** Inserts and retrieves metric records using parameterized SQL queries to prevent SQL injection.
* **Automated Unit Testing:** Includes high-coverage test suites built with `pytest`, utilizing in-memory SQLite databases (`:memory:`) for isolated database testing.
* **Clean Architecture:** Strict separation of concerns between business logic (`src/`), database management, and CLI interface (`main.py`).

---

## Project Structure

```text
py-data-processor/
├── src/
│   ├── __init__.py
│   ├── data_processor.py   # Text analysis logic & JSON generation
│   └── db_manager.py       # SQLite connection manager & CRUD queries
├── tests/
│   ├── test_data_processor.py # Unit tests for file operations
│   └── test_db_manager.py   # In-memory unit tests for SQL operations
├── main.py                 # Interactive CLI interface
├── requirements.txt        # Environment dependencies
├── .gitignore              # Ignored files (DBs, caches, venv)
└── README.md               # Project documentation
Getting Started
Prerequisites
Python 3.10+ installed

Git

Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/mawerendev/py-data-processor.git](https://github.com/mawerendev/py-data-processor.git)
cd py-data-processor
Create and activate a virtual environment:

Windows (PowerShell):

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the main CLI application:

Bash
python main.py
Follow the on-screen menu to ingest text data into the database or retrieve historical processing records.

Running Automated Tests
To execute the complete test suite using pytest:

Bash
python -m pytest
Author
mawerendev - GitHub Profile
