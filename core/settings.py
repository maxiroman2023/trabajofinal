from django.urls import reverse_lazy
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ubru$o6!4*&!3!1jfr+)va1x*l21$viks9i_eb418tgcsf=ky('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['maxiroman.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    "crispy_forms",
    "crispy_bootstrap5",


    'core',
    'acercaDe',
    'articulo',    
    'comentarios',
    'contacto',
    'usuarios',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

LOGIN_REDIRECT_URL = reverse_lazy('home') #redirigirá un usuario después de que haya iniciado sesión correctamente en el sistema.
LOGOUT_REDIRECT_URL = reverse_lazy('home') #se aplica cuando un usuario ha cerrado sesión en el sistema
LOGIN_URL = reverse_lazy('usuarios:login_user') #redirigirá a un usuario que intente acceder a una vista o recurso que requiere autenticación, pero que aún no ha iniciado sesión.

AUTH_USER_MODEL = 'usuarios.User' #extender ese modelo o utilizar un modelo personalizado.



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'




##############################################################################

# settings.py

# Configuración para el backend de correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Configuración para el servidor de correo (SMTP)
# Aquí debes proporcionar los detalles de tu servidor de correo saliente (SMTP)
# En este ejemplo, se muestra cómo configurarlo para Gmail. Reemplaza con tus propios valores.
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 8000
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'test@gmail.com'
EMAIL_HOST_PASSWORD = 'django123'

# Configuración para mostrar correos en consola durante el desarrollo
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


##############################################################################

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Archivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

#MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = "home/USUARIO/PROYECTO/static"
MEDIA_ROOT = "home/USUARIO/PROYECTO/media"

MEDIA_URL = '/media/'

LOGIN_URL = '/signin/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

