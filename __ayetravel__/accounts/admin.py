from django.contrib import admin
from accounts.models import UserProfile, UserNotifications

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserNotifications)
# admin.site.register(UserCalendar)
