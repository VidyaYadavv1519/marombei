"""
Marombei created by Danilo Marto de Carvalho <danilomartodecarvalho@protonmail.com>
Copyright© Webtinguetá Project licensed under the MIT Agreement.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
