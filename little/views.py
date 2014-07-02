from django.http import Http404
from django.shortcuts import redirect

from .models import Short


def short_detail(request, short_key):
    try:
        short = Short.objects.get_for_key(short_key)
    except Short.DoesNotExist as e:
        raise Http404(e.message)

    if short.destination:
        return redirect(short.destination)

    return redirect(short.image.url)
