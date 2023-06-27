from django.urls import path
from .consumers import chatroom

ws_urlpatterns = [
    path("ws/chat/<str:room_name>",chatroom.as_asgi())
]