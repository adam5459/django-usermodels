from django.urls import  path
from .views import room, home, createRoom, updateRoom
urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>', room , name='room'),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>', updateRoom, name='update-room'),

]