from rest_framework import serializers
from .models import ScrapingJob


class ScrapingJobSerializer(serializers.ModelSerializer):
    target_url_value = serializers.CharField(source="target_url.url", read_only=True)
    project_name = serializers.CharField(source="target_url.project.name", read_only=True)

    class Meta:
        model = ScrapingJob
        fields = [
            "id",
            "target_url",
            "target_url_value",
            "project_name",
            "name",
            "frequency",
            "status",
            "last_run_at",
            "next_run_at",
            "total_runs",
            "successful_runs",
            "failed_runs",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "target_url_value",
            "project_name",
            "last_run_at",
            "next_run_at",
            "total_runs",
            "successful_runs",
            "failed_runs",
            "created_at",
            "updated_at",
        ]