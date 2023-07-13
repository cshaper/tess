from .base import * #noqa
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="S_DSS6aFdKzoocC-I6PMbflDAjVDVi94wZ3dNg8gLtkO-vAHYsA",
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS =["http://localhost:8080"]

