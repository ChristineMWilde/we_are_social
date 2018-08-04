from base import *
import os
import dj_database_url
import settings
 
DEBUG = False
 
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_huXVMABXPzJmtBClroUo7vFA')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_qgkn8rHXvHGEtPaqreOCeXi7')

 
SITE_URL = 'https://code-institute-social-wilde.herokuapp.com'
ALLOWED_HOSTS.append('code-institute-social-wilde.herokuapp.com')
 
# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}