import os

# Add this line to read DJANGO_ALLOWED_HOSTS env var
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')
