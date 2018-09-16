from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


app_name = 'community'


urlpatterns = [
    # url(r'^$', CommunityTripsList.as_view(), name='community_trips_list'),
    # url(r'^trips/(?P<slug>[\w-]+)/$', CommunityTripDetailed.as_view(), name='community_trips_detailed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
