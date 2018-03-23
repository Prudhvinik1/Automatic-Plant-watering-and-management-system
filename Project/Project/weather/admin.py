from django.contrib import admin
from .models import Weather,Plant,Waterlevel,plantid
# Register your models here.

admin.site.register(Weather)
admin.site.register(plantid)
admin.site.register(Plant)
admin.site.register(Waterlevel)
