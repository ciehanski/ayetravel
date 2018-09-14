from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Trips, TravelLogs
from app.forms import CreateTripForm
from django.urls import reverse_lazy
from login.models import UserNotifications
from django.shortcuts import get_object_or_404


def render_user_notifications(request):
    notifs = []
    for notif in UserNotifications.objects.all():
        if notif.user_id.get_username() == request.user.get_username():
            notifs.append(notif)
    return notifs


def render_user_trips(request):
    trips = []
    for trip in Trips.objects.all():
        if trip.user_id.get_username() == request.user.get_username():
            trips.append(trip)
    return trips


def render_community_trips():
    community_trips = []
    for trip in Trips.objects.all():
        if trip.public:
            community_trips.append(trip)
    return community_trips


class IndexView(LoginRequiredMixin, TemplateView):
    context_object_name = 'index'
    template_name = '../../app/templates/app/index.html'

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips()
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return self.render_to_response(context)


class TravelLogList(LoginRequiredMixin, ListView):
    context_object_name = 'travel_log_list'
    template_name = '../../app/templates/app/travel_log.html'
    queryset = TravelLogs.objects.all()


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = 'trips_list'
    template_name = '../../app/templates/app/trips_list.html'
    queryset = Trips.objects.all()


class CommunityTripsList(LoginRequiredMixin, ListView):
    context_object_name = 'community_trips_list'
    template_name = '../../app/templates/app/trips_list.html'
    queryset = render_community_trips()


class CommunityTripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'community_trips_detailed'
    template_name = '../../app/templates/app/trips_detailed.html'
    queryset = render_community_trips()

    def get_object(self, queryset=Trips):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'trips_detailed'
    template_name = '../../app/templates/app/trips_detailed.html'
    queryset = Trips.objects.all()

    def get_object(self, queryset=Trips):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)


class CreateTrip(LoginRequiredMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    form_class = CreateTripForm
    fields = '__all__'

    def get_object(self, queryset=Trips):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(LoginRequiredMixin, UpdateView):
    context_object_name = 'update_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    # form_class = UpdateTripForm
    fields = '__all__'

    def get_object(self, queryset=Trips):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(LoginRequiredMixin, DeleteView):
    context_object_name = 'update_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    success_url = reverse_lazy('app:trips_list')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)

    def post(self, request, *args, **kwargs):
        pass


class CalendarView(LoginRequiredMixin, DetailView):
    context_object_name = 'calendar'
    template_name = '../../app/templates/app/calendar.html'


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
