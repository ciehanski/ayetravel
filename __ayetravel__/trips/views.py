from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trips.models import Trips
from app.views import render_user_trips, render_community_trips, render_user_notifications


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'trips_detailed'
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


class CreateTrip(LoginRequiredMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = 'trips/create_trip.html'
    object = Trips
    model = Trips
    fields = '__all__'

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

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(LoginRequiredMixin, UpdateView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    model = Trips
    fields = '__all__'

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

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(LoginRequiredMixin, DeleteView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    model = Trips
    success_url = reverse_lazy('app:trips_list')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Trips, id=id_)

    def post(self, request, *args, **kwargs):
        pass


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = 'trips_list'
    template_name = 'trips/trips_list.html'
    object_list = Trips.objects.all()

    def get(self, request, **kwargs):
        self.object_list = render_user_trips(request)
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips()
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return self.render_to_response(context)
