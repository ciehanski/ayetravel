from django.conf.urls import url
from trips.views import TripsList, TripsDetailed, UpdateTrip, CreateTrip, DeleteTrip
from django.conf import settings
from django.conf.urls.static import static

# TEMPLATE TAGGING
app_name = 'trips'

urlpatterns = [
    url(r'^$', TripsList.as_view(), name='trips_list'),
    url(r'^create/$', CreateTrip.as_view(), name='create_trip'),
    url(r'^(?P<slug>[\w-]+)/$', TripsDetailed.as_view(), name='trips_detailed'),
    url(r'^update/(?P<slug>[\w-]+)/$', UpdateTrip.as_view(), name='update_trip'),
    url(r'^delete/(?P<slug>[\w-]+)/$', DeleteTrip.as_view(), name='delete_trip'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
