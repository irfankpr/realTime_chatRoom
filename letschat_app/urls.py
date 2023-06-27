from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("chatroom/<str:room>/",views.chatroom,name='chatroom')
]
