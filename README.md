# TodoWoo - Django Todo List Application

A full-featured todo list application built with Django, featuring user authentication, task management, and importance ratings.

## Features

- **User Authentication**
  - User registration and login
  - Protected mode to disable new registrations
  - Secure password handling

- **Todo Management**
  - Create, view, edit, and delete todos
  - Mark todos as complete
  - Importance rating system (1-5)
  - Add memo/notes to todos

- **Organization**
  - Current todos view (incomplete tasks)
  - Completed todos view with timestamps
  - Pagination for better performance
  - Sort by importance and completion date

## Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite3
- **Frontend**: Bootstrap 5.3.8
- **Authentication**: Django built-in auth system

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todowoo-project
   ```

2. **Create and activate virtual environment**

   Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment configuration**

   Create a `.env` file in the project root:
   ```env
   # Optional: Set to true to disable new user registrations
   PROTECTED_MODE=false
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Configuration

### Environment Variables

Create a `.env` file in the project root directory:

```env
# Protected Mode - Disable new user registrations
PROTECTED_MODE=false
```

### Local Settings

For local development, create `todowoo/local_settings.py`:

```python
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

This file overrides production settings and is ignored by git.

## Usage

### Creating Todos

1. Log in to your account
2. Click "New" in the navigation bar
3. Fill in the todo details:
   - Title (required)
   - Memo (optional)
   - Importance (1-5, default: 1)
4. Click "Save"

### Managing Todos

- **View Current Todos**: Click "Current" to see incomplete tasks
- **View Completed Todos**: Click "Completed" to see finished tasks
- **Edit Todo**: Click on any todo to edit its details
- **Complete Todo**: Click the "Complete" button on a todo
- **Delete Todo**: Click the "Delete" button on a todo

### Protected Mode

When `PROTECTED_MODE=true` in your `.env` file:
- New user registrations are disabled
- Signup links are hidden from the interface
- Users attempting to access signup see a modal error message
- Existing users can still log in normally

## Project Structure

```
todowoo-project/
├── todo/                          # Main application
│   ├── migrations/               # Database migrations
│   ├── static/todo/              # Static files (CSS, JS, images)
│   ├── templates/todo/           # HTML templates
│   ├── context_processors.py    # Custom context processors
│   ├── forms.py                 # Form definitions
│   ├── models.py                # Data models
│   └── views.py                 # View logic
├── todowoo/                      # Project configuration
│   ├── constants.py             # Global constants
│   ├── settings.py              # Production settings
│   ├── urls.py                  # URL routing
│   └── wsgi.py                  # WSGI configuration
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Development

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test todo
```

### Database Management

```bash
# Create new migration after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View SQL for a migration
python manage.py sqlmigrate todo 0001
```

### Admin Interface

Access the Django admin interface at `/admin/` to:
- Manage users
- View and edit todos
- Monitor application data

## Security Features

- CSRF protection on all forms
- User-specific todo access (users can only see their own todos)
- Password validation and hashing
- SQL injection protection through Django ORM
- XSS protection through template escaping

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Credits

Created by [Six Hills AI](https://sixhills.ai)

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.
