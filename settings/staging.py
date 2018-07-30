from base import *
 
DEBUG = False
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_huXVMABXPzJmtBClroUo7vFA')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_qgkn8rHXvHGEtPaqreOCeXi7')

 
SITE_URL = 'https://code-institute-social-cw.herokuapp.com'
ALLOWED_HOSTS.append('code-institute-social-cw.herokuapp.com')
 
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