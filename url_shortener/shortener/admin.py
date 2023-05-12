from django.contrib import admin
from .models import URL

# Register your models here.


class URLAdmin(admin.ModelAdmin):
    list_display = (
        "original_url",
        "short_url",
        "access_count",
        "created_at",
        "last_access",
    )
    readonly_fields = list_display
    search_fields = ("original_url", "short_url")

    def delete_selected(self, request, queryset):
        queryset.delete()

    delete_selected.short_description = "Delete selected URLs"


admin.site.register(URL, URLAdmin)
