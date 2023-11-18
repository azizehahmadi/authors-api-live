from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-_g#8hzmc!&z!l_vkkfli&r8bt#7o8_@^n)!locw0-7az)ziltc",
)

ALLOWED_HOSTS = ['*']



