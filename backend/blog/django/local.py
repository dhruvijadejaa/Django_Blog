from .base import *

DEBUG = True

ALLOWED_HOSTS = [

    "localhost",

    "127.0.0.1",

]

CORS_ALLOWED_ORIGINS = [

    "http://localhost:5173",  # Vite React app

    "http://127.0.0.1:8000",

]

# Development database (if different from production)

# DATABASES = {

#     "default": {

#         "ENGINE": "django.db.backends.sqlite3",

#         "NAME": BASE_DIR / "db.sqlite3",

#     }

# }

# Send emails to the console instead of actually sending them

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Optional: Disable secure settings locally

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = False