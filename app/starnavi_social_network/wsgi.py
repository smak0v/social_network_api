"""
WSGI config for starnavi_social_network project
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starnavi_social_network.settings')

application = get_wsgi_application()
