from rest_framework import serializers
from .models import Location, Weather

class LocationSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Location
        fields = ['id', 'city', 'country']

class WeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only= True)
    class Meta:
        model = Weather
        fields = ['id', 'location','temperature', 'humidity', 'weather_condition']


