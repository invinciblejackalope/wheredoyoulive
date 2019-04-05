"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# https://stackoverflow.com/questions/17688594/how-to-diff-between-local-uncommitted-changes-and-origin

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/eng/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-i$r$vp^#n!wk2%9d5ag2_2yl%d)!1+2z5^$2=4kh4zlvi_i6l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'wheredoyoulive.apps.WheredoyouliveConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'project1.urls'

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

WSGI_APPLICATION = 'project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
# https://stackoverflow.com/questions/3602450/where-are-my-postgres-conf-files
# https://stackoverflow.com/questions/11919391/postgresql-error-fatal-role-username-does-not-exist
# https://stackoverflow.com/questions/21122598/postgres-user-does-not-exist
# https://dba.stackexchange.com/questions/1285/how-do-i-list-all-databases-and-tables-using-psql
# https://www.postgresql.org/docs/8.2/sql-dropdatabase.html
# https://stackoverflow.com/questions/20198235/postgresql-could-not-create-any-tcp-ip-sockets-mavericks
# https://stackoverflow.com/questions/7975414/how-to-check-status-of-postgresql-server-mac-os-x
# https://superuser.com/questions/553045/fatal-lock-file-postmaster-pid-already-exists
# https://stackoverflow.com/questions/5598517/find-the-host-name-and-port-using-psql-commands
# https://stackoverflow.com/questions/29937378/django-db-utils-operationalerror-could-not-connect-to-server
# https://stackoverflow.com/questions/35455109/cant-run-the-server-on-django-connection-refused
# https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python
# https://stackoverflow.com/questions/3582552/postgresql-connection-url
# https://stackoverflow.com/questions/30897442/django-1-8-fails-to-django-db-utils-programmingerror-relation-auth-user-does
# https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git

# instructions:
# > install postgres, psycopg2, dj_database_url
# pg_ctl -D /usr/local/var/postgres start
# createdb database
# psql database
# > your prompt should now be database=#
# CREATE USER databaseuser WITH PASSWORD 'password';
# ALTER ROLE databaseuser SET client_encoding TO 'utf8';
# ALTER ROLE databaseuser SET default_transaction_isolation TO 'read committed';
# ALTER ROLE databaseuser SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE database TO databaseuser;
# \q
# > set the environment variable DATABASE_URL to
# postgres://databaseuser:password@localhost:5432/database
# > now python manage.py runserver should be good! yay

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=False)
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
