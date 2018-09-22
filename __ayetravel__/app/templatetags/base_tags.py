from django import template
from accounts.models import UserNotifications
from trips.models import Trips, Pins

register = template.Library()


@register.simple_tag
def notifications(request):
    for notif in UserNotifications.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        yield notif


def get_total_notifs(request):
    for _ in UserNotifications.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        yield 1


@register.simple_tag
def user_trips(request):
    for trip in Trips.objects.all().filter(
            user_id__username__iexact=request.user.get_username()).order_by('modified_at'):
        yield trip


@register.simple_tag
def trips_detail_tag(request):
    for trip in Trips.objects.all():
        if trip.user_id.username == request.user.get_username() or trip.public:
            yield trip


@register.simple_tag
def community_trips(request):
    for trip in Trips.objects.all().filter(public=True).filter(
            user_id__username__iexact=request.user.get_username()).order_by('pins_total'):
        yield trip


@register.simple_tag
def pins_tag(request):
    for pin in Pins.objects.all().filter(user_id__username__iexact=request.user.get_username()):
        yield pin
