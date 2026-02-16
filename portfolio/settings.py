"""
Django settings for portfolio project.
"""

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# SECURITY
# ==========================
SECRET_KEY = os.environ.get("SECRET_KEY")
if SECRET_KEY is None:
    if DEBUG := os.environ.get("DEBUG", "False") == "True":
        SECRET_KEY = "django-insecure-dev-key-change-in-production"
    else:
        raise ValueError("SECRET_KEY environment variable is required in production")

DEBUG = os.environ.get("DEBUG", "False") == "True"

# Railway + local development hosts
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS", "localhost,127.0.0.1,.railway.app"
).split(",")

# ==========================
# APPLICATIONS
# ==========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "core",
]

# ==========================
# REST FRAMEWORK
# ==========================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# ==========================
# MIDDLEWARE
# ==========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"

# ==========================
# DATABASE
# ==========================
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    # Railway / production
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL, conn_max_age=600, ssl_require=True
        )
    }
else:
    # Local development fallback
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "mydb"),
            "USER": os.environ.get("POSTGRES_USER", "myuser"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "mypassword"),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", 5432),
        }
    }

# ==========================
# PASSWORD VALIDATION
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==========================
# INTERNATIONALIZATION
# ==========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==========================
# STATIC FILES
# ==========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==========================
# MEDIA FILES
# ==========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==========================
# DEFAULT PRIMARY KEY
# ==========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# CORS
# ==========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
if frontend_url := os.environ.get("FRONTEND_URL"):
    if frontend_url not in CORS_ALLOWED_ORIGINS:
        CORS_ALLOWED_ORIGINS.append(frontend_url)

CORS_ALLOW_CREDENTIALS = True

# ==========================
# CSRF (important for admin + cross-origin requests)
# ==========================
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.railway.app",
]
if frontend_url := os.environ.get("FRONTEND_URL"):
    if frontend_url not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(frontend_url)

# ==========================
# SECURITY SETTINGS
# ==========================
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

if not DEBUG:
    # Railway is behind a proxy
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = False          # Railway already forces HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True