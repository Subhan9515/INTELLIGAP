
"""
Django settings for intelligap project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# Security settings
# --------------------------------------------------

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-local-development-key-only'
)

DEBUG = os.environ.get('RENDER') is None

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

if os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.environ['RENDER_EXTERNAL_HOSTNAME'])


# --------------------------------------------------
# Application definition
# --------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Existing IntelliGap apps
    'accounts',
    'chatbot',
]


# --------------------------------------------------
# Middleware
# --------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------------------------
# URLs
# --------------------------------------------------

ROOT_URLCONF = 'intelligap.urls'


# --------------------------------------------------
# Templates
# --------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --------------------------------------------------
# WSGI
# --------------------------------------------------

WSGI_APPLICATION = 'intelligap.wsgi.application'


# --------------------------------------------------
# Database
# --------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --------------------------------------------------
# Password validation
# --------------------------------------------------

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


# --------------------------------------------------
# Internationalization
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# --------------------------------------------------
# Static files
# --------------------------------------------------

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}


# --------------------------------------------------
# Default primary key field type
# --------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --------------------------------------------------
# MSG91 Configuration
# --------------------------------------------------

MSG91_AUTHKEY = os.environ.get(
    'MSG91_AUTHKEY',
    'YOUR_MSG91_AUTHKEY'
)

MSG91_TEMPLATE_ID = os.environ.get(
    'MSG91_TEMPLATE_ID',
    'YOUR_TEMPLATE_ID'
)


# --------------------------------------------------
# Media files
# --------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
