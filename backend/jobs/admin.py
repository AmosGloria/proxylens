from django.contrib import admin
from .models import ScrapingJob


@admin.register(ScrapingJob)
class ScrapingJobAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "target_url",
        "frequency",
        "status",
        "total_runs",
        "successful_runs",
        "failed_runs",
        "last_run_at",
        "created_at",
    ]
    search_fields = ["name", "target_url__url"]
    list_filter = ["frequency", "status", "created_at"]