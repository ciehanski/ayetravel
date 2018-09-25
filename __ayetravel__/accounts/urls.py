from django.conf.urls import url
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import CalendarView

# TEMPLATE TAGGING
app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='index'),
    url(r'^index.html', views.ProfileView.as_view()),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^(?P<username>[\w-]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^recovery/$', views.RecoveryView.as_view(), name='recovery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
