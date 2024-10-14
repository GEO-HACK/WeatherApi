from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather , name = 'weather'),
    path('weather/<int:id>', views.weather_details, name= 'weather_details')
]