from config import get_settings

from pay_sim.settings.base import (
    BASE_DIR,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    STATIC_URL,
)


DEBUG = False

SECRET_KEY = get_settings().secret_key

ALLOWED_HOSTS = get_settings().allowed_hosts

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_settings().db_name,
        "USER": get_settings().db_user,
        "PASSWORD": get_settings().db_password,
        "HOST": get_settings().db_host,
        "PORT": get_settings().db_port,
    }
}

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
