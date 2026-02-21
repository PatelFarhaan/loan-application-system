# Loan Application

A loan application management system built with Flask and MySQL. Users can submit loan applications through a web form, and administrators can view all applications with their approval status.

## Tech Stack

- **Language:** Python 3
- **Framework:** Flask
- **Database:** MySQL (via PyMySQL)
- **ORM:** SQLAlchemy (Flask-SQLAlchemy)
- **Migrations:** Flask-Migrate (Alembic)
- **Templating:** Jinja2

## Features

- Loan application form with comprehensive fields (personal info, loan amount, purpose)
- Server-side form validation with user-friendly error messages
- Application status dashboard showing all submissions
- Randomized approval status simulation
- File attachment support for loan documents
- Database migrations with Alembic
- Blueprint-based modular architecture

## Prerequisites

- Python 3.7+
- MySQL
- pip

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Loan_App
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:5000`.

## Environment Variables

| Variable       | Description                   | Example                                           |
|----------------|-------------------------------|---------------------------------------------------|
| `SECRET_KEY`   | Flask secret key for sessions | `a-random-secret-string`                          |
| `DATABASE_URI` | MySQL connection string       | `mysql+pymysql://root:password@localhost/loan`     |

## Project Structure

```
Loan_App/
├── app.py                          # Application entry point
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
├── Dockerfile                      # Docker configuration
├── Makefile                        # Common development commands
├── Loan APP report.pdf             # Project documentation
├── migrations/                     # Alembic database migrations
│   ├── alembic.ini
│   ├── env.py
│   └── versions/
└── project/
    ├── __init__.py                 # App factory, DB config, blueprints
    ├── models.py                   # Application model
    ├── core/
    │   ├── views.py                # Routes (loan form, status page)
    │   └── templates/
    │       ├── loanapp.html        # Loan application form
    │       └── loanstatus.html     # Application status dashboard
    └── templates/                  # Shared templates
```

## API Endpoints

| Method | Endpoint     | Description                             |
|--------|--------------|-----------------------------------------|
| GET    | `/loanapp`   | Loan application form                   |
| POST   | `/loanapp`   | Submit a loan application               |
| GET    | `/status`    | View all applications with status       |

## License

This project is licensed under the MIT License.
