from .base import* 

ALLOWED_HOSTS = ['ecommerce-2-dimitard.c9users.io'] 


STATIC_URL = '/static/'  
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 