from django.urls import path
from . import views

temp = 'temp'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path("data/", views.get_data, name="get_data"),
    path('temp', views.temp, name='temp'),
    path('ultra', views.ultra, name='ultra'),
]