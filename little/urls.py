from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(
        r'^(?P<short_key>[a-z\d]+)/$',
        'little.views.short_detail',
        name='short_detail'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
