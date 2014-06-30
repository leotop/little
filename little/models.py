from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Short(models.Model):
    destination = models.URLField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='%y/%m/%d/')
    created_by = models.ForeignKey(get_user_model())
    created_at = models.DateTimeField(default=timezone.now)
