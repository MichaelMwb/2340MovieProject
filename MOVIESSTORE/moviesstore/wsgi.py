"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# filepath: /c:/Users/micha/OneDrive/CS-2340/2340MovieProject/MOVIESSTORE/moviesstore/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MOVIESSTORE.moviesstore.settings')

application = get_wsgi_application()
