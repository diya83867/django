"""
Django settings for mergeall project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from django.contrib.messages import constants as messages
# from oauth2client.client import flow_from_clientsecrets
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=q#ua3*hqxf&h-zp66x)j_o7@b4621=w%2abp5z23lfcyiy33^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'channels',
    'easyaudit',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'corsheaders',
    'blog',
    'pollapp',
    'channelapp'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', )
}

crispy_template_pack ='bootstrap5'

MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'blog.middleware.ErrorHandlerMiddleware',
]

ROOT_URLCONF = 'mergeall.urls'

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

WSGI_APPLICATION = 'mergeall.wsgi.application'
ASGI_APPLICATION = 'mergeall.asgi.application'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases






#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'test',
#        'HOST': 'database-1.cxqi4eki0k95.ap-south-1.rds.amazonaws.com',
#        'PORT' : '5432',
#        'USER' : 'postgres',
#        'PASSWORD' : 'mysql1234',
#    }
#} 




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}






# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

# Base url to serve media files
MEDIA_URL = '/media/'
# Path where media is stored
MEDIA_ROOT = BASE_DIR / 'media/'

AUTH_USER_MODEL = "blog.User"
AUTHENTICATION_BACKENDS = ('mergeall.backends.EmailAuthBackend','django.contrib.auth.backends.ModelBackend','allauth.account.auth_backends.AuthenticationBackend')
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'blog:login'
LOGOUT_URL = 'blog:logout'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
CORS_ORIGIN_ALLOW_ALL = True

SITE_ID = 1
# REST_USE_JWT = True 
# FLOW = flow_from_clientsecrets(
#     settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
#     scope='https://www.googleapis.com/auth/gmail.readonly',
#     redirect_uri='http://127.0.0.1:8000/oauth2callback',
#     prompt='consent')

GOOGLE_OAUTH2_CLIENT_SECRETS_JSON = 'client_secrets.json'












