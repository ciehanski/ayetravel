from django.conf.urls import url
from app import views
from django.conf import settings
from django.conf.urls.static import static

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html', views.IndexView.as_view()),
    url(r'^community/trips/$', views.CommunityTripsList.as_view(), name='community_list'),
    url(r'^community/trips/(?P<pk>\d+)/$', views.CommunityTripsDetailed.as_view(), name='community_trips_detailed'),
    url(r'^my/trips/$', views.TripsList.as_view(), name='trips_list'),
    url(r'^my/trips/create/$', views.CreateTrip.as_view(), name='create_trip'),
    url(r'^my/trips/(?P<pk>\d+)/$', views.TripsDetailed.as_view(), name='trips_detailed'),
    url(r'^my/trips/update/(?P<pk>\d+)/$', views.UpdateTrip.as_view(), name='update_trip'),
    url(r'^my/trips/delete/(?P<pk>\d+)/$', views.DeleteTrip.as_view(), name='delete_trip'),
    url(r'^my/calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^my/travellogs/$', views.TravelLogList.as_view(), name='travel_log_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
