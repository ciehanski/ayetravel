from django.conf.urls import url
from app.views import SearchView, IndexView, CalendarView
from django.conf import settings
from django.conf.urls.static import static

# TEMPLATE TAGGING
app_name = 'app'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^index.html', IndexView.as_view()),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^my/calendar/$', CalendarView.as_view(), name='calendar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
