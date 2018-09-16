from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from trips.models import Trips
from app.views import render_community_trips, render_user_trips, render_user_notifications


class CommunityTripsList(LoginRequiredMixin, ListView):
    context_object_name = 'community_trips_list'
    template_name = 'trips/trips_list.html'
    object_set = render_community_trips()

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips()
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return self.render_to_response(context)


class CommunityTripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'community_trips_detailed'
    template_name = 'trips/trips_detailed.html'
    object = Trips

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips()
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return self.render_to_response(context)

    def get_object(self, queryset=Trips):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)
