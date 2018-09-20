from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from trips.models import Trips
from app.views import IndexView


class CommunityTripsList(IndexView, ListView):
    context_object_name = 'community_trips_list'
    template_name = 'community/community_list.html'
    object_list = Trips.objects.all()


class CommunityTripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'community_trips_detailed'
    template_name = 'trips/trips_detailed.html'
    object = Trips

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)
