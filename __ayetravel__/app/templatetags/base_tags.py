from django import template
from django.db.models import Q
from accounts.models import UserNotifications
from trips.models import Trips, Participants

register = template.Library()


@register.simple_tag
def get_notifications(request):
    for notif in UserNotifications.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('timestamp'):
        yield notif


@register.simple_tag
def get_total_user_notifs(request):
    return UserNotifications.objects.all().filter(user_id__username__iexact=request.user.get_username()).count()


@register.simple_tag
def get_user_trips(request):
    for trip in Trips.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('modified_at'):
        yield trip


@register.simple_tag
def get_total_user_trips(request):
    return Trips.objects.all().filter(user_id__username__iexact=request.user.get_username()).count()


@register.simple_tag
def get_trips_detail(request):
    for trip in Trips.objects.all():
        if trip.user_id.username == request.user.get_username() or trip.public:
            yield trip


@register.simple_tag
def get_community_trips(request):
    for trip in Trips.objects.all().filter(public=True).filter(~Q(
            user_id__username__iexact=request.user.get_username())).order_by('pins_total'):
        yield trip


@register.simple_tag
def get_participants(request):
    for participant in Participants.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('modified_at'):
        yield participant
