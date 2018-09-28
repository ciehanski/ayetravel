from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserNotifications
from trips.models import Trips, Participants


class BaseViewMixin(LoginRequiredMixin, object):
    context_object_name = 'base'
    template_name = 'app/base.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = get_notifications(request)
        context['user_trips'] = get_user_trips(request)
        context['community_trips'] = get_community_trips(request)
        context['notif_total'] = get_total_user_notifs(request)
        context['total_user_trips'] = get_total_user_trips(request)
        context['participants'] = get_participants(request)

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


class IndexView(BaseViewMixin, TemplateView):
    context_object_name = 'index'
    template_name = 'app/index.html'


class SearchView(BaseViewMixin, ListView):
    context_object_name = 'search'
    template_name = 'app/search.html'
    object_list = Trips.objects.all()


class CalendarView(BaseViewMixin, TemplateView):
    context_object_name = 'calendar'
    template_name = 'app/calendar.html'


def get_notifications(request):
    for notif in UserNotifications.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('timestamp'):
        yield notif


def get_total_user_notifs(request):
    return UserNotifications.objects.all().filter(user_id__username__iexact=request.user.get_username()).count()


def get_total_user_trips(request):
    return Trips.objects.all().filter(user_id__username__iexact=request.user.get_username()).count()


def get_community_trips(request):
    for trip in Trips.objects.all().filter(public=True).filter(~Q(
            user_id__username__iexact=request.user.get_username())).order_by('pins_total'):
        yield trip


def get_participants(request):
    for participant in Participants.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('modified_at'):
        yield participant


# def get_trips_detail(request):
#     for trip in Trips.objects.all():
#         if trip.user_id.username == request.user.get_username() or trip.public:
#             yield trip


def get_user_trips(request):
    for trip in Trips.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('modified_at'):
        yield trip


def handler404(request):
    return render(request, 'app/404.html', status=404)


def handler500(request):
    return render(request, 'app/500.html', status=500)
