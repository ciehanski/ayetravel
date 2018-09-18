from django.conf.urls import url
from app.views import SearchView, IndexView, CalendarView
from django.conf import settings
from django.conf.urls.static import static
from community.views import CommunityTripsList, CommunityTripsDetailed

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^index.html', IndexView.as_view()),
    url(r'^community/trips/$', CommunityTripsList.as_view(), name='community_list'),
    url(r'^community/trips/(?P<slug>[\w-]+)/$', CommunityTripsDetailed.as_view(), name='community_trips_detailed'),
    url(r'^my/calendar/$', CalendarView.as_view(), name='calendar'),
    url(r'^search/$', SearchView.as_view(), name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
