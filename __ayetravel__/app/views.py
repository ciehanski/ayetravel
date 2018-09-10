from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    context_object_name = 'index'
    template = '../../app/templates/app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/index.html')


class TripsList(LoginRequiredMixin, TemplateView):
    context_object_name = 'trips_list'
    template = '../../app/templates/app/trips_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/trips_list.html')


class TripsDetailed(LoginRequiredMixin, TemplateView):
    context_object_name = 'trips_detailed'
    template = '../../app/templates/app/trips_detailed.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/trips_detailed.html')


class CreateTrip(LoginRequiredMixin, FormView):
    context_object_name = 'create_trip'
    template = '../../app/templates/app/create_trip.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/create_trip.html')


class CalendarView(LoginRequiredMixin, TemplateView):
    context_object_name = 'calendar'
    template = '../../app/templates/app/calendar.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/calendar.html')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
