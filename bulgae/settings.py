"""
Django settings for bulgae project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from environs import Env

env = Env()
env.read_env()

ENGINE = env('DB_ENGINE')
DATABASE = env('DB_NAME')
USER = env('DB_USER')
PASSWORD = env('DB_PASSWORD')
HOST = env('DB_HOST')
PORT = env('DB_PORT')
DJANGO_SK = env('DJANGO_SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SK

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definitionus

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'hanja.apps.HanjaConfig',
    'korean.apps.KoreanConfig',
    'hanja_korean.apps.HanjaKoreanConfig',
    'english.apps.EnglishConfig',
    'hanja_english.apps.HanjaEnglishConfig',
    'french.apps.FrenchConfig',
    'hanja_french.apps.HanjaFrenchConfig',
    'hanja_association.apps.HanjaAssociationConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bulgae.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bulgae.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + ENGINE,
        'NAME': DATABASE,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    "DEFAULT_MODEL_RENDERING": "example"
}

# Constants
HTTP_CONSTANTS = {
    'SUCCESS': 200,
    'CREATED': 201,
    'BAD_REQUEST': 400,
    'UNAUTHENTICATED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'NOT_ALLOWED': 405,
    'INTERNAL_SERVER_ERROR': 500,
}

ROLES = {
    'ROLE_USER': 1,
    'ROLE_ADMIN': 2,
    'ROLE_SUPER_ADMIN': 3,
    'ROLE_ORGANIZATION_OWNER': 4,
    'ROLE_ORGANIZATION_CO_OWNER': 5,
    'ROLE_ORGANIZATION_MEMBER': 6,
    'ROLE_TEAM_LEADER': 7,
    'ROLE_TEAM_MEMBER': 8,
}
