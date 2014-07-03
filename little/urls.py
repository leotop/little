from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views


admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^create/',
        views.short_create,
        name='short_create'),

    url(
        r'^(?P<short_key>[a-z\d]+)/$',
        views.short_detail,
        name='short_detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
