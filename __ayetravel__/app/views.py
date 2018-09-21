from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from trips.models import Trips, Pins
from accounts.models import UserNotifications, UserProfile
from django import template


class IndexView(LoginRequiredMixin, TemplateView):
    context_object_name = 'index'
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifs'] = notifications_tag(request)
        context['trips_total'] = len(user_trips(request))
        context['notifs_total'] = len(notifications_tag(request))
        # Search handling
        search_term = request.GET.get('search')
        if search_term is not None:
            search = Trips.objects.filter(name__icontains=search_term)
            if len(search) > 0:
                trips = []
                for trip in search:
                    trips.append(trip)
                context['search_results'] = trips
                return render(request, 'app/search.html', context)
            else:
                context['error'] = 'Nothing matched your search.'
                return render(request, 'app/search.html', context)
        else:
            # if search was blank, just re-render index page
            return render(request, self.template_name, context)


class SearchView(IndexView, ListView):
    context_object_name = 'search'
    template_name = 'app/search.html'
    object_list = Trips.objects.all()


class CalendarView(IndexView, TemplateView):
    context_object_name = 'calendar'
    template_name = 'app/calendar.html'


register = template.Library()


@register.simple_tag
def notifications_tag(request):
    notifs = []
    for notif in UserNotifications.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        notifs.append(notif)
    return notifs


@register.simple_tag
def user_trips(request):
    trips = []
    for trip in Trips.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        trips.append(trip)
    return trips


@register.simple_tag
def trips_detail_tag(request):
    trips = []
    for trip in Trips.objects.all():
        if trip.user_id.username == request.user.get_username() or trip.public:
            trips.append(trip)
    return trips


@register.simple_tag
def community_trips(request):
    com_trips = []
    for trip in Trips.objects.all().filter(public=True):
        if trip.user_id.username != request.user.get_username():
            com_trips.append(trip)
    return com_trips


@register.simple_tag
def pins_tag(request):
    pins_ = []
    for pin in Pins.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        pins_.append(pin)
    return pins_


def handler404(request):
    return render(request, 'app/404.html', status=404)


def handler500(request):
    return render(request, 'app/500.html', status=500)
