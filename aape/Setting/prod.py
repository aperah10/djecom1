from .base import * 

with open(os.path.join(BASE_DIR,'secret.txt')) as f :
    SECRET_KEY= f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['djecomfirst.herokuapp.com','aperahwork.herokuapp.com',]

INSTALLED_APPS += [
   'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'accounts',
    'customer',
    'product',
    'restapi',
    
]




