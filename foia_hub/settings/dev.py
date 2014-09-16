from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS = (
    'debug_toolbar',
) + INSTALLED_APPS

DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r"^(?!debug_toolbar/).*"

INTERNAL_IPS = ('127.0.0.1',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


try:
    from .local_settings import *
except ImportError:
    pass