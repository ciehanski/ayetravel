from django.contrib import admin
from accounts.models import UserProfile, UserNotifications, UserCalendar

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserNotifications)
admin.site.register(UserCalendar)
