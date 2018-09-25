from django import template
from accounts.models import InsensitiveUser

register = template.Library()


@register.simple_tag
def get_current_user(request):
    return InsensitiveUser.objects.all().filter(username__iexact=request.user.get_username())
