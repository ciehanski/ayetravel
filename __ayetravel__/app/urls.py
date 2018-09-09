from django.conf.urls import url
from app import views

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html', views.IndexView.as_view()),
    url(r'^mytrips/', views.TripsList.as_view(), name='trips_list'),
    url(r'^mytrips/create/', views.CreateTrip.as_view(), name='create_trip'),
    url(r'^mytrips/trip/$', views.TripsDetailed.as_view(), name='trips_detailed'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
]
