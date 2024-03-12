"""
Django settings for time_budget project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "y29$br=r$pjt2q_hqnua9tb-gm9ii$ihvel8zlp8g$bo-$$hd)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "django-env3.eba-3jbfuszg.us-west-2.elasticbeanstalk.com",
    "127.0.0.1",
    "*",
]

# Application definition

INSTALLED_APPS = [
    "timeapp",
    "front_end",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",  # for api
    "corsheaders",  # for api
    # authenticaion
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django.contrib.sites",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {"google": {"EMAIL_AUTHENTICATION": True}}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "443267133087-6nfqf70g0koidhvga5ojcjj8cqvj8hqk.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]
SITE_ID = 1

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Assuming your React frontend runs on this URL
    "https://yourfrontenddomain.com",
    "http://*",
]

ROOT_URLCONF = "time_budget.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "allauth.account.context_processors.account",
                # "allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]

WSGI_APPLICATION = "time_budget.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "timedatabase",
        "USER": "admin",
        "PASSWORD": "Parr0tdr0ne",
        "HOST": "time-database.c90aio8gg9bc.us-west-1.rds.amazonaws.com",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# gmail password: ixhm uvmi iogn wkbb

# set up email server
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "marksoulkid@gmail.com"  # Your Gmail address
EMAIL_HOST_PASSWORD = (
    "ixhm uvmi iogn wkbb"  # Your Gmail password or app-specific password
)


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

# Redirect to index page after login
LOGIN_REDIRECT_URL = "/index/"

# Redirect to home page after logout
LOGOUT_REDIRECT_URL = "/"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"  # The default - so could be left out altogether

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "front_end/build/static"),
    os.path.join(BASE_DIR, "timeapp/static"),
]

REACT_APP_BUILD_PATH = "front_end/build/"
