import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "htmx_websockets.settings")

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi_application,
    # Just HTTP for now. (We will add ws later)
})