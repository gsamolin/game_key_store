import os
from pathlib import Path

# Set up the Django project structure
BASE_DIR = Path(__file__).resolve().parent.parent  # The base directory of the project

# Secret key for cryptographic signing (change this for production)
SECRET_KEY = 'your-secret-key-here'

# Debug mode (should be False in production)
DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# Hosts allowed to connect to this Django instance
ALLOWED_HOSTS = []

# Installed apps in the project
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin interface
    'django.contrib.auth',  # Authentication framework
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static file management
    'store', # Adding the store app
    'rest_framework',  # Adding Django REST framework
    'corsheaders',
]

# Middleware for processing requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages user sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against Cross-Site Request Forgery
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
    'corsheaders.middleware.CorsMiddleware',
]

# Root URL configuration for the project
ROOT_URLCONF = 'game_key_store.urls'

# Template settings for rendering HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add paths to custom template directories here
        'APP_DIRS': True,  # Automatically look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Adds request object to templates
                'django.contrib.auth.context_processors.auth',  # Adds user object to templates
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point for the project
WSGI_APPLICATION = 'game_key_store.wsgi.application'

# Database configuration (using SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to SQLite database file
    }
}

# Password validation settings for authentication
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Default language code

TIME_ZONE = 'UTC'  # Default time zone

USE_I18N = True  # Enable internationalization

USE_TZ = True  # Enable timezone support

# URL for serving static files
STATIC_URL = 'static/'

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
