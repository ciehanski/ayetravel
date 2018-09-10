from django.contrib import admin
from django.apps import AppConfig
from models import Trips

#
# class AppConfig(AppConfig):
#     name = 'app'


admin.site.register(Trips)
