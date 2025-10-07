## Recipe Rover - A FastAPI Recipe Finder
A simple web application that allows users to manage a personal recipe book. Users can add recipes, view them, and find new recipes based on the ingredients they have.

## Tech Stack
Backend: FastAPI

Database: SQLite

Frontend: Jinja2, HTML, CSS

## How to Run Locally
1. Navigate to the project directory:
```
cd src/sameera731-recipe-rover/
```

(Optional) Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```
pip install fastapi "uvicorn[standard]" jinja2 python-multipart
```

3. Start the development server:
```
uvicorn main:app --reload
```
4. View the webapp:
Open your browser to http://127.0.0.1:8000.