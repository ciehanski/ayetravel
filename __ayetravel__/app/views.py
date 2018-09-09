from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template = '../../app/templates/app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/index.html')


class TripsList(LoginRequiredMixin, TemplateView):
    template = '../../app/templates/app/trips_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/trips_list.html')


class TripsDetailed(LoginRequiredMixin, TemplateView):
    template = '../../app/templates/app/trips_detailed.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/trips_detailed.html')


class CreateTrip(LoginRequiredMixin, TemplateView):
    template = '../../app/templates/app/create_trip.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/create_trip.html')


class CalendarView(LoginRequiredMixin, TemplateView):
    template = '../../app/templates/app/calendar.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../app/templates/app/calendar.html')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
