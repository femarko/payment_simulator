from pay_sim.settings.base import (
    BASE_DIR,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    STATIC_URL,
)

SECRET_KEY = 'django-insecure-r!g-um+ook+ek4-1$%=vj2m$tzgm5r19xd@@%f_i2@yx^f6z!s'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
