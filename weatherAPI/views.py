from django.shortcuts import render
from django.http import JsonResponse
from .models import Location, Weather
from .serializers import LocationSerializer,WeatherSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def weather(request):
    if request.method == 'GET':
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many= True)

        return JsonResponse(serializer.data, safe= False)

@api_view(['GET','PUT','DELETE'])
def weather_details(request, id):
    try:
        weather = Weather.objects.get(pk=id)

    except Weather.DoesNotExist:

        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WeatherSerializer(weather)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = WeatherSerializer(weather, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        weather.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



    
