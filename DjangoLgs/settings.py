"""
Django settings for DjangoLgs project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@63&#y2242bx9z_^ep8oi2yl(b7^@4hgrs(&_=1avoh90i=-ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
     
    'django.contrib.admin', # installazione grappelli vedere qui: https://django-grappelli.readthedocs.io/en/latest/quickstart.html
    'django_crontab',  # crontab app
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'grappelli', # installazione grappelli vedere qui: https://django-grappelli.readthedocs.io/en/latest/quickstart.html
    #'admin_searchable_dropdown', #per aggiungere dropdown in admin panel https://pypi.org/project/django-admin-searchable-dropdown/
    #'leaflet',
   # 'leaflet_admin_list',
    # 'django_admin_geomap', # djangi admingeomap # https://github.com/vb64/django.admin.geomap
    # 'django.contrib.gis', # gis module
    'app', #app connected to django-importexport
    #'django_google_maps',
    #'djangocms_gmaps',

    'dbbackup',  # django-dbbackup
    'import_export',#library for import expor to add after installation
    
    # Other apps…
    'phonenumber_field',
    

]



DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage' #dbbackup setting
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR/'backup'} #dbbackup setting

CRONJOBS = [ ('*/60 * * * *', 'DjangoLgs.cron.my_backup') ] # crontab settings

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'DjangoLgs.urls'

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
# Our settings
GRAPPELLI_SWITCH_USER = True

WSGI_APPLICATION = 'DjangoLgs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# installazione di postgreSQL: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} """


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auditor',
        'USER': 'mauro9916',
        'PASSWORD': 'testpass123',
        'HOST': 'localhost',
        'PORT': '',
    }
    
 }

""" DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker', #'user001',
        'PASSWORD': 'docker', #'123456789',
        'HOST': '127.0.0.1',
        'PORT': '25432'
    }
}
 """
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
STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles"  #new

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_ROOT = [BASE_DIR/"media"]



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
GOOGLE_MAPS_API_KEY = 'AIzaSyATANps-5vRV-NB99qLHwvTat7GZKAn8SI'
EASY_MAPS_GOOGLE_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ___0123456789'

LOCATION_FIELD = {
# Impostazioni per provider opestreet
'map.provider': 'openstreetmap',
'search.provider': 'nominatim',

#Impostazione per provider google
   #  'map.provider': 'google',
   # 'map.zoom': 13,
   # 'search.provider': 'google',
   # '   search.suffix': '',
    # Google
    #'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    # 'provider.google.api_key': '',
    # 'provider.google.api_libraries': '',
    # 'provider.google.map.type': 'ROADMAP',
    
    
    # Mapbox
    # 'provider.mapbox.access_token': '',
    # 'provider.mapbox.max_zoom': 18,
   #  'provider.mapbox.id': 'mapbox.streets',
   
   
    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 22,
    
    
    # misc
   #'resources.root_path': LOCATION_FIELD_PATH,
   # 'resources.media': {
   # 'js': (
   # LOCATION_FIELD_PATH + '/js/form.js',
   # ),  
    #} # vedere Qui a pg 8: https://readthedocs.org/projects/django-location-field/downloads/pdf/latest/
}
 

