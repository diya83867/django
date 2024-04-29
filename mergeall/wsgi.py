"""
WSGI config for mergeall project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
# import sys

# sys.path.insert(0, '/var/www/projects/django-merge-project')
# sys.path.insert(1, '/var/www/projects/virtual/blogenv/lib/python3.10/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mergeall.settings')

application = get_wsgi_application()
