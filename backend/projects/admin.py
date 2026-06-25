from django.contrib import admin
from .models import Project, TargetURL


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "domain", "is_active", "created_at"]
    search_fields = ["name", "domain", "owner__username"]
    list_filter = ["is_active", "created_at"]


@admin.register(TargetURL)
class TargetURLAdmin(admin.ModelAdmin):
    list_display = ["url", "project", "is_active", "last_checked_at", "created_at"]
    search_fields = ["url", "project__name"]
    list_filter = ["is_active", "created_at"]