import random
import string

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

import base32_crockford


API_KEY_LENGTH = 32


def generate_key(length):
    return ''.join(
        random.choice(string.digits + string.ascii_lowercase)
        for __ in xrange(length))


class ShortManager(models.Manager):
    def get_for_key(self, key):
        return self.get(key=key)


class Short(models.Model):
    key = models.CharField(blank=True, max_length=100, null=True)
    destination = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='%y/%m/%d/')
    created_by = models.ForeignKey(get_user_model())
    created_at = models.DateTimeField(default=timezone.now)

    objects = ShortManager()

    def __unicode__(self):
        if self.destination:
            return self.destination

        return self.image.url

    def save(self, *args, **kwargs):
        super(Short, self).save(*args, **kwargs)

        if not self.key:
            self.key = base32_crockford.encode(self.pk)
            self.save()


class APIKey(models.Model):
    user = models.ForeignKey(get_user_model())
    key = models.CharField(max_length=API_KEY_LENGTH, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = generate_key(API_KEY_LENGTH)

        super(APIKey, self).save(*args, **kwargs)
