from django.conf.urls import url
from app import views

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html', views.IndexView.as_view()),
    url(r'^mytrips/', views.TripsList.as_view(), name='trips_list'),
    url(r'^mytrips/create/', views.CreateTrip.as_view(), name='create_trip'),
    url(r'^mytrips/trip/(?P<pk>\d+)/$', views.TripsDetailed.as_view(), name='trips_detailed'),
    url(r'^mytrips/trip/update/(?P<pk>\d+)/$', views.UpdateTrip.as_view(), name='update_trip'),
    url(r'^mytrips/trip/delete/(?P<pk>\d+)/$', views.DeleteTrip.as_view(), name='delete_trip'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^mytravellogs/', views.TravelLogList.as_view(), name='travel_log_list'),
]
