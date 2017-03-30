"""
[`source`_]

Production Django settings for Cyphon.

For more information on this Django file, see:
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of Django settings and their values, see:
https://docs.djangoproject.com/en/1.9/ref/settings/

.. _source: ../_modules/cyphon/settings/prod.html

"""

# standard library
import logging
import os

# local
from .base import *

LOGGER = logging.getLogger(__name__)

DEBUG = False

ADMINS = [
    # ('Jane Smith', 'jane@example.com'),
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

#: URL for constructing link with MEDIA_URL, e.g. https://www.example.com
BASE_URL = 'https://localhost:8000'

# LOG_DIR = '/var/log/cyphon'
LOG_DIR = BASE_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'when': 'midnight',
            'interval': 1,
            'backupCount': '7',
            'formatter': 'verbose',
        },
        'receiver_file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'receiver.log'),
            'when': 'midnight',
            'interval': 1,
            'backupCount': '7',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.server': {
            'handlers': ['console', 'file', 'mail_admins'],
            'propagate': True,
            'level': 'WARNING'
        },
        'django.request': {
            'handlers': ['console', 'file', 'mail_admins'],
            'propagate': True,
            'level': 'WARNING'
        },
        'django': {
            'handlers': ['console', 'file', 'mail_admins'],
            'propagate': True,
            'level': 'WARNING',
        },
        'receiver': {
            'handlers': ['console', 'receiver_file', 'mail_admins'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}
