"""
Django settings for pjt project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-8ipj=(!((lb90+bjty%4fgx(o()ckknq0(=b!udv$)_xyzj%u#"
SECRET_KEY = os.getenv("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
ALLOWED_HOSTS = [
    "Kdtfinalpjt-env.eba-fky28zqx.ap-northeast-2.elasticbeanstalk.com",
    "127.0.0.1",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    "storages",
    "channels",
    "daphne",
    "chat",
    "comments",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "imagekit",
    "django_bootstrap5",
    "book",
    "accounts",
    "review",
    "notes",
    "taggit.apps.TaggitAppConfig",
    "taggit_templatetags2",
]
# Channels
# # channels.layers.InMemoryChannelLayer??
# channels_redis.core.RedisChannelLayer
# "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
WSGI_APPLICATION = "pjt.wsgi.application"
ASGI_APPLICATION = "pjt.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        # },
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pjt.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "notes.context_processors.counter",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
AUTH_USER_MODEL = "accounts.User"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# DEBUG = True


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "kdt_djangor_rds",  # 코드 블럭 아래 이미지 참고하여 입력
#         "USER": "postgres",
#         "PASSWORD": "qwerasdf1234",  # 데이터베이스 생성 시 작성한 패스워드
#         "HOST": "kdt-final-pjt-rds.chhzgju7hfuj.ap-northeast-2.rds.amazonaws.com",  # 코드 블럭 아래 이미지 참고하여 입력
#         "PORT": "5432",
#     }
# }
DEBUG = os.getenv("DEBUG") == "True"
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    #     DEFAULT_FILE_STORAGE = "pjt.storages.MediaStorage"

    #     AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    #     AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    #     AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    #     AWS_REGION = "ap-northeast-2"
    #     AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
    #         AWS_STORAGE_BUCKET_NAME,
    #         AWS_REGION,
    #     )

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),  # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),  # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"),  # .env 파일에 value 작성
            "PORT": "5432",
        }
    }
