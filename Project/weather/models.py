from django.db import models

# Create your models here.
class Weather(models.Model):
    temperature = models.CharField(max_length = 5)
    humidity = models.CharField(max_length = 5)
    check = models.CharField(max_length = 8)
    pub_date = models.DateTimeField('date published')

class plantid(models.Model):
    pid = models.IntegerField(primary_key = True)
    plant_name = models.CharField(max_length = 25,null=True)
    latitude = models.CharField(max_length = 10,null=True)
    longitude = models.CharField(max_length = 10,null=True)
    def __str__(self):
        return str(self.pid)

class Plant(models.Model):
    pid = models.ForeignKey(plantid,null=True)
    moisture = models.CharField(max_length = 8,null=True)

class Waterlevel(models.Model):
    #reading = models.CharField(max_length = 10)
    #bucket = models.CharField(max_length = 10)
    water_level = models.CharField(max_length = 10)

