from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from travellogs.models import TravelLogs
from app.views import render_community_trips, render_user_trips, render_user_notifications


class TravelLogList(LoginRequiredMixin, ListView):
    context_object_name = 'travel_log_list'
    template_name = 'travellogs/travel_log.html'
    queryset = TravelLogs.objects.all()

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips()
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return self.render_to_response(context)
