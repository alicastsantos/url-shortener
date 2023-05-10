from django.contrib import admin
from .models import URL

# Register your models here.


class URLAdmin(admin.ModelAdmin):
    list_display = ("original_url", "short_url", "created_at", "access_count")
    readonly_fields = ("short_url", "access_count", "created_at")


admin.site.register(URL, URLAdmin)
