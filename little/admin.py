from django.contrib import admin

from .models import Short


class ShortAdmin(admin.ModelAdmin):
    list_display = ('key', 'destination', 'image', 'created_by', 'created_at', )
    model = Short


admin.site.register(Short, ShortAdmin)
