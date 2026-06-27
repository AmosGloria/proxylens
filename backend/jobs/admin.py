from django.contrib import admin
from .models import ScrapingJob


@admin.register(ScrapingJob)
class ScrapingJobAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "target_url",
        "frequency",
        "status",
        "run_status",
        "total_runs",
        "successful_runs",
        "failed_runs",
        "last_run_at",
        "created_at",
    ]
    search_fields = ["name", "target_url__url", "last_task_id"]
    list_filter = ["frequency", "status", "run_status", "created_at"]
    readonly_fields = [
        "last_task_id",
        "last_run_at",
        "next_run_at",
        "total_runs",
        "successful_runs",
        "failed_runs",
        "last_error_message",
        "created_at",
        "updated_at",
    ]