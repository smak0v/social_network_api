"""
ASGI config for starnavi_social_network project
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'starnavi_social_network.settings')

application = get_asgi_application()
