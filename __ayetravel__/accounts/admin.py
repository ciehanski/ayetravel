from django.contrib import admin
from accounts.models import Profile, UserNotifications, InsensitiveUser, UserCalendar

# Register your models here.
admin.site.register(InsensitiveUser)
admin.site.register(Profile)
admin.site.register(UserNotifications)
admin.site.register(UserCalendar)
