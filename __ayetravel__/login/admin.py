from django.contrib import admin
from login.models import UserSettings, UserNotifications

# Register your models here.
admin.site.register(UserSettings)
admin.site.register(UserNotifications)