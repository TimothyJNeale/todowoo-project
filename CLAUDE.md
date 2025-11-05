# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TodoWoo is a Django-based todo list application with user authentication and task management. Users can create, view, edit, complete, and delete todos with importance ratings (1-5).

## Development Commands

### Setup
```bash
# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

### Running the Application
```bash
# Run development server
python manage.py runserver

# Access at http://127.0.0.1:8000/
# Admin interface at http://127.0.0.1:8000/admin/
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

### Testing
```bash
# Run tests
python manage.py test

# Run tests for specific app
python manage.py test todo
```

## Architecture

### Project Structure
- **todowoo/** - Main project configuration
  - `settings.py` - Production settings with local_settings override pattern
  - `local_settings.py` - Local development overrides (DEBUG=True, ALLOWED_HOSTS=[])
  - `urls.py` - Root URL configuration
  - `constants.py` - Global constants (e.g., MAX_TODOS_PER_PAGE)

- **todo/** - Main application
  - `models.py` - Todo model with user association, importance (1-5), timestamps
  - `views.py` - All view logic including auth and CRUD operations
  - `forms.py` - TodoForm for model-based form handling
  - `templates/todo/` - HTML templates using Django template language
  - `static/todo/` - Static assets (logo, CSS, JS)

### Authentication Flow
- Custom signup/login views using Django's built-in User model
- Login redirects to `currenttodos` view
- Logout redirects to `home` view
- All todo views require `@login_required` decorator
- User authentication configured in settings:
  - LOGIN_URL = 'loginuser'
  - LOGIN_REDIRECT_URL = 'currenttodos'
  - LOGOUT_REDIRECT_URL = 'home'

### Todo Management
- **Current todos**: Filtered by `datecompleted__isnull=True`, ordered by `-importance`
- **Completed todos**: Filtered by `datecompleted__isnull=False`, paginated (10 per page), ordered by `-datecompleted`
- **Navigation context**: Views use `next` parameter to return users to previous page after create/edit
- **Security**: All queries filtered by `user=request.user` to prevent unauthorized access

### Data Model
```python
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    importance = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

### URL Patterns
All URLs are defined in `todowoo/urls.py` (no app-level urls.py):
- Auth: `/signup/`, `/login/`, `/logout/`
- Todos: `/create/`, `/current/`, `/completed/`, `/todo/<id>/`, `/todo/<id>/complete`, `/todo/<id>/delete`

### Settings Configuration
- Production settings in `settings.py` (DEBUG=False, specific ALLOWED_HOSTS)
- Local overrides via `local_settings.py` import pattern
- Use `sixhills/local_settings_stub.py` as template for new local_settings.py
- SQLite database: `db.sqlite3`
- Static files: `STATIC_ROOT = BASE_DIR / 'static'`
- Media files: `MEDIA_ROOT = BASE_DIR / 'media'`

### Pagination
Completed todos use Django's Paginator with constant from `todowoo.constants.MAX_TODOS_PER_PAGE`

## Key Implementation Patterns

### View-level Authorization
All todo operations use `get_object_or_404(Todo, pk=todo_pk, user=request.user)` to ensure users can only access their own todos.

### Navigation Flow
Create and edit forms accept a `next` parameter to redirect users back to the page they came from (currenttodos or completedtodos).

### Form Validation
Forms use Django's built-in validation. Invalid submissions re-render with form errors (no custom error handling beyond ValueError catches).
