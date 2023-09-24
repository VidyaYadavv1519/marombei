"""
Marombei created by Danilo Marto de Carvalho <danilomartodecarvalho@protonmail.com>
Copyright© Webtinguetá Project licensed under the MIT Agreement.
"""

from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as dburl

# Core Settings
################################################################################
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Debuging
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DEBUG
DEBUG = config("DEBUG", cast=bool)

# Cache
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        # https://docs.djangoproject.com/en/4.2/ref/settings/#location
        "LOCATION": config("CACHE_URL"),
    }
}

# Database
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATABASES
DATABASES = {"default": config("DATABASE_URL", cast=dburl)}
# https://docs.djangoproject.com/en/4.2/ref/settings/#atomic-requests
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Email
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_BACKEND
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_HOST
EMAIL_HOST = config("EMAIL_HOST")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_HOST_PASSWORD
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_HOST_USER
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_PORT
EMAIL_PORT = config("EMAIL_PORT")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-EMAIL_USE_TLS
EMAIL_USE_TLS = config("EMAIL_USE_TLS")

# File Uploads
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-FILE_UPLOAD_HANDLERS
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-MEDIA_ROOT
MEDIA_ROOT = str(BASE_DIR / "media/")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-MEDIA_URL
MEDIA_URL = "media/"
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Globalization
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-LANGUAGE_CODE
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-LOCALE_PATHS
LOCALE_PATHS = [str(BASE_DIR / "locale")]
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-TIME_ZONE
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-USE_I18N
USE_I18N = True
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-USE_TZ
USE_TZ = True

# HTTP
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-INTERNAL_IPS
INTERNAL_IPS = [
    "127.0.0.1",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-WSGI_APPLICATION
WSGI_APPLICATION = "config.wsgi.application"

# Models
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-FIXTURE_DIRS
FIXTURE_DIRS = [str(BASE_DIR / "fixtures")]
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY
SECRET_KEY = config("SECRET_KEY")
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-X_FRAME_OPTIONS
X_FRAME_OPTIONS = "DENY"

# Serialization
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DEFAULT_CHARSET
DEFAULT_CHARSET = "utf-8"

# Templates
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-TEMPLATES
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/4.2/ref/settings/#dirs
        "DIRS": [],
        # https://docs.djangoproject.com/en/4.2/ref/settings/#app-dirs
        "APP_DIRS": True,
        # https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-TEMPLATES-OPTIONS
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Testing
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-TEST_RUNNER
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# URLs
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-ROOT_URLCONF
ROOT_URLCONF = "config.urls"

# Auth
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-user-model
AUTH_USER_MODEL = "auth.User"
# https://docs.djangoproject.com/en/4.2/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Sites
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#site-id
SITE_ID = 1

# Static Files
################################################################################
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/4.2/ref/settings/#static-url
STATIC_URL = "static/"
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
