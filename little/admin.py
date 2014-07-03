from django.contrib import admin

from .models import APIKey, Short


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', )
    model = APIKey


class ShortAdmin(admin.ModelAdmin):
    list_display = (
        'key', 'destination', 'image', 'created_by', 'created_at', )
    model = Short


admin.site.register(APIKey, APIKeyAdmin)
admin.site.register(Short, ShortAdmin)
