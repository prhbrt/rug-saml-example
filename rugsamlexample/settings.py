import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['rugsamlexample-dev2.jzxrtdh3tt.eu-west-1.elasticbeanstalk.com']
SECRET_KEY = '1&!h_59t55cq%byi(01(+p2_g^xd2v-no$3rzc8xe7i=3ihhl6'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_saml2_auth',
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

ROOT_URLCONF = 'rugsamlexample.urls'

LOGIN_URL='accounts/login'

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

WSGI_APPLICATION = 'rugsamlexample.wsgi.application'

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rugsamlexample',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



SAML2_AUTH = {
    'METADATA_AUTO_CONF_URL': 'https://tst-idp.id.rug.nl/nidp/saml2/metadata',
    'DEFAULT_NEXT_URL': '/admin',
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],
        'ACTIVE_STATUS': True,
        'STAFF_STATUS': True,
        'SUPERUSER_STATUS': False,
    },
    'ATTRIBUTES_MAP': {
        'email': 'urn:mace:dir:attribute-def:mail',
        'username': 'urn:mace:dir:attribute-def:uid',
        'first_name': 'urn:mace:dir:attribute-def:givenName',
        'last_name': 'urn:mace:dir:attribute-def:sn',
    },
    # 'ASSERTION_URL': 'https://cosmo.service.rug.nl',
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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
