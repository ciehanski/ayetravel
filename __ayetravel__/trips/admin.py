from django.contrib import admin
from trips.models import Trips, Comments, Excursions, Participants, Pins, DailyLog, Itinerary

admin.site.register(Trips)
admin.site.register(Comments)
admin.site.register(Excursions)
admin.site.register(Participants)
admin.site.register(Pins)
admin.site.register(DailyLog)
admin.site.register(Itinerary)
