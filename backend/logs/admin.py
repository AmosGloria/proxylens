from django.contrib import admin
from .models import RequestLog


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = [
        "url",
        "job",
        "status",
        "status_code",
        "response_time_ms",
        "retry_count",
        "created_at",
    ]
    search_fields = ["url", "job__name", "error_message"]
    list_filter = ["status", "status_code", "created_at"]