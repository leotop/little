from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from .models import APIKey, Short, Visit


def short_detail(request, short_key):
    try:
        short = Short.objects.get_for_key(short_key)
    except Short.DoesNotExist as e:
        raise Http404(e.message)

    Visit.objects.create(
        short=short,
        remote_addr=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        referrer=request.META.get('HTTP_REFERER'),
    )

    if short.destination:
        return redirect(short.destination)

    return redirect(short.image.url)


def short_create(request):
    url = request.GET.get('url')
    api_key = request.GET.get('key')
    user = APIKey.objects.get(key=api_key).user

    short, __ = Short.objects.get_or_create(
        destination=url,
        created_by=user,
    )

    domain = get_current_site(request).domain
    short_path = reverse('short_detail', kwargs={'short_key': short.key})
    short_url = '{scheme}://{domain}{short_path}'.format(
        scheme=settings.SHORT_SCHEME,
        domain=domain,
        short_path=short_path)

    return HttpResponse(short_url, content_type='text/plain')
