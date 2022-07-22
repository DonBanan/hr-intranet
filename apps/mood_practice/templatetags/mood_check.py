from datetime import date

from django import template

from ..models import Niko


register = template.Library()


@register.simple_tag
def mood_check(user, day, *args, **kwargs):
    if Niko.objects.filter(user=user, created_at__date=day).exists():
        return Niko.objects.get(user=user, created_at__date=day)
    else:
        return False
