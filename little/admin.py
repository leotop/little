from django.contrib import admin

from .models import APIKey, Short, Visit


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', )
    model = APIKey


class VisitAdmin(admin.TabularInline):
    extra = 0
    model = Visit
    readonly_fields = ('remote_addr', 'user_agent', 'referrer', 'created_at', )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ShortAdmin(admin.ModelAdmin):
    inlines = (VisitAdmin, )
    list_display = (
        'key', 'destination', 'image', 'created_by', 'created_at', )
    model = Short


admin.site.register(APIKey, APIKeyAdmin)
admin.site.register(Short, ShortAdmin)
