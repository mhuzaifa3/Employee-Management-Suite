# Employee Management Suite

A lightweight **Flask + SQLite** web application to manage employees with basic CRUD operations.  
Built as a personal project to demonstrate backend and full-stack development skills.  

## Features
- Add, update, delete, and list employees  
- Search employees by name or phone  
- Pagination for large employee lists  
- Flash messages for feedback (success/error)  
- SQLite database (auto-created in `instance/`)  
- Simple Bootstrap 5 frontend  
- Basic service layer for clean architecture  
- Pytest tests for core functionality  

## Getting Started

1. **Clone the repo**:
   ```
   git clone https://github.com/mhuzaifa3/Employee-Management-Suite.git
   ```
2. **Create & activate the virtual environment**:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
4. **Run the app**:
   ```
   python run.py
   ```
5. **Access the Application**:Open a web browser and navigate to `http://localhost:5000` to access the Employee Management Suite.
