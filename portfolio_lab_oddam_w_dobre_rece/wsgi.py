"""
WSGI config for portfolio_lab_oddam_w_dobre_rece project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_lab_oddam_w_dobre_rece.settings')

application = get_wsgi_application()
