from django.conf.urls import url
from login import views

# TEMPLATE TAGGING
app_name = 'login'

urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='index'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/index.html', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^recovery/', views.RecoveryView.as_view(), name='recovery'),
]
