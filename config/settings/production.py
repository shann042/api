# SECURITY WARNING: keep the secret key used in production secret!

from os import getenv,path
from dotenv import load_dotenv
from .base import *
from .base import BASE_DIR

local_env_file=path.join(BASE_DIR,".envs",".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)
    
# DEBUG = True

# SITE_NAME =getenv("SITE_NAME")

SECRET_KEY=getenv("DJANGO_SECRET_KEY")






ALLOWED_HOSTS = []
ADMINS=[("Shanmuga","m.shanmuga@gmail.com"),]
# ADMIN_URL=getenv("DJANGO_ADMIN_URL")

# EMAIL_BACKEND="djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST=getenv("EMAIL_HOST")
# EMAIL_PORT=getenv("EMAIL_PORT")
# DEFAULT_FROM_EMAIL=getenv("DEFAULT_FROM_EMAIL")
# DOMAIN=getenv("DOMAIN")