python
# --------------------------------------------------
# Security settings — Render and local development
# --------------------------------------------------

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-local-development-key-only'
)

if os.environ.get('DEBUG') is not None:
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
else:
    DEBUG = not (
        os.environ.get('RENDER')
        or os.environ.get('VERCEL')
        or os.environ.get('VERCEL_ENV')
    )

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
    'intelligap.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://intelligap.onrender.com',
]
