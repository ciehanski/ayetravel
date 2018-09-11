from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Trips, TravelLogs
from app.forms import CreateTripForm
from django.urls import reverse_lazy
import airbnb


class IndexView(LoginRequiredMixin, ListView):
    context_object_name = 'index'
    template_name = '../../app/templates/app/index.html'
    model = Trips

    # def get(self, request, *args, **kwargs):
    #     airbnb_listings = airbnb.main('-asa', 'Indianapolis')
    #     return airbnb_listings


class TravelLogList(LoginRequiredMixin, ListView):
    context_object_name = 'travel_log_list'
    template_name = '../../app/templates/app/travel_log.html'
    model = TravelLogs


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = 'trips_list'
    template_name = '../../app/templates/app/trips_list.html'
    model = Trips


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'trips_detailed'
    template_name = '../../app/templates/app/trips_detailed.html'
    model = Trips


class CreateTrip(LoginRequiredMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    fields = '__all__'

    form = CreateTripForm()

    def post(self, request, *args, **kwargs):
        form = CreateTripForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return TripsList(request)
        else:
            print('Create Trip - Form invalid')
            return render(request, '../../app/templates/app/create_trip.html', {'form': form})


class UpdateTrip(LoginRequiredMixin, UpdateView):
    context_object_name = 'update_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    fields = ['user_location', 'date', 'budget', 'participants']


class DeleteTrip(LoginRequiredMixin, DeleteView):
    context_object_name = 'update_trip'
    template_name = '../../app/templates/app/create_trip.html'
    model = Trips
    success_url = reverse_lazy('app:trips_list')


class CalendarView(LoginRequiredMixin, TemplateView):
    context_object_name = 'calendar'
    template_name = '../../app/templates/app/calendar.html'


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
