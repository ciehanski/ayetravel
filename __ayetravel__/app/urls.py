from django.conf.urls import url
import travellogs.views
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from community.views import CommunityTripsList, CommunityTripsDetailed

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index.html', views.IndexView.as_view()),
    url(r'^community/trips/$', CommunityTripsList.as_view(), name='community_list'),
    url(r'^community/trips/(?P<slug>[\w-]+)/$', CommunityTripsDetailed.as_view(), name='community_trips_detailed'),
    url(r'^my/calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^my/travellogs/$', travellogs.views.TravelLogList.as_view(), name='travel_log_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
