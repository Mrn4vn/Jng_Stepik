'''
ASGI config  for library project.

It exposes the ASGI callable as a module-level variable named application,

For more info on this file, ask your mom, lol)
'''

import os

from jango.core.asgi import get_asgi_application

os.onviron.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

application = get_asgi_application()