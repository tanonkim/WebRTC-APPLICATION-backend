from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/call/<str:room_name>', consumers.VideoCallConsumer.as_asgi())
]