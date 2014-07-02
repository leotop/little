from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

import crockford


class ShortManager(models.Manager):
    def get_for_key(self, key):
        pk = crockford.b32decode(str(key).upper())
        return self.get(pk=pk)


class Short(models.Model):
    destination = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='%y/%m/%d/')
    created_by = models.ForeignKey(get_user_model())
    created_at = models.DateTimeField(default=timezone.now)

    objects = ShortManager()

    def __unicode__(self):
        if self.destination:
            return self.destination

        return self.image.url

    def key(self):
        return crockford.b32encode(unicode(self.pk)).lower()
