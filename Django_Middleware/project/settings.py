from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'j6i9j7rf6@u^-tmc7=lqz)8@v_26*@0=l-b)80@&t(45#oe-!s'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user_manage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'user_manage.auth_middleware.CustomAuthMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "CONN_MAX_AGE": 600,
        'NAME': "middleware",
        'USER': "middleware",
        'PASSWORD': "password",
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

SIMPLE_JWT = {
    # Lifetime of Access Token, which is used for authentication headers
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    # Lifetime of Access Token, which is used for getting a new Auth Token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    # After claiming a new Access token, do we want a new Refresh Token too?
    'ROTATE_REFRESH_TOKENS': True,
    # After Rotation of Refresh Token, do we want to blacklist (block) the old Token?
    'BLACKLIST_AFTER_ROTATION': False,
    # Using either Symmetric or Asymmetric Algo to Sign the Tokens
    'ALGORITHM': 'HS256',
    # The key which will be used During Signing of Token
    'SIGNING_KEY': SECRET_KEY,
    # In case of Asymmetric, this will be used to very the tokens
    'VERIFYING_KEY': None,
    # The header name that will be check to get the Access Token. HTTP_AUTHORIZATION -> Authorization
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # The Prefix for the Access Token. AUTH_HEADER_NAME: AUTH_HEADER_TYPES (Access_Token)
    'AUTH_HEADER_TYPES': ('Bearer',),
    # The name of column from the preferred users table. The column value should not change for particular
    # user. The preferred value is name of PK column for the table. If any changes, then clashes are
    # possible
    'USER_ID_FIELD': 'id',
    # The key against the value for 'USER_ID_FIELD'. Key value will will be stored under
    # object of refresh_token.access_token.payload['USER_ID_CLAIM'] = USER_ID_FIELD
    'USER_ID_CLAIM': 'user_id',
    # Using only AccessToken. Refer Token Types from docs
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # Key for the type of token. Refer Token types in Docs
    'TOKEN_TYPE_CLAIM': 'token_type',
}
