# Online Market Platform

A Django-based online marketplace platform that allows users to buy and sell items, manage their listings, and communicate with other users.

## Features

- User authentication and authorization
- Item listing and management
- Dashboard for user activities
- Messaging system between users
- Media handling for item images
- Responsive design

## Project Structure

The project consists of several Django apps:
- `core`: Core functionality and base templates
- `item`: Item listing and management
- `dashboard`: User dashboard and activity tracking
- `conversation`: Messaging system between users

## Prerequisites

- Python 3.x
- Django 5.0.4
- SQLite3 (default database)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd online_market
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application at `http://127.0.0.1:8000/`

## Testing

Run the test suite:
```bash
python manage.py test core
```

## Project Configuration

- Debug mode is enabled by default (not recommended for production)
- SQLite3 is used as the database
- Media files are stored in the `media/` directory
- Static files are served from the `static/` directory

## Security Notes

- The project uses Django's built-in security features
- CSRF protection is enabled
- Session middleware is configured
- Password validation is implemented

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request



