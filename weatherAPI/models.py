from django.db import models

class Location (models.Model):
   city = models.CharField(max_length=200)
   country = models.CharField(max_length=50)

   def __str__(self):
        return self.city

class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather_details')
    temperature = models.FloatField()
    humidity = models.FloatField()
    weather_condition = models.CharField(max_length=50)
    

    def __str__(self):
        return self.weather_condition