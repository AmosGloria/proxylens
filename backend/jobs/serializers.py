from rest_framework import serializers
from .models import ScrapingJob


class ScrapingJobSerializer(serializers.ModelSerializer):
    target_url_value = serializers.CharField(source="target_url.url", read_only=True)
    project_name = serializers.CharField(source="target_url.project.name", read_only=True)

    success_rate = serializers.SerializerMethodField()

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
            "run_status",
            "last_task_id",
            "last_run_at",
            "next_run_at",
            "total_runs",
            "successful_runs",
            "failed_runs",
            "success_rate",
            "last_error_message",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "target_url_value",
            "project_name",
            "run_status",
            "last_task_id",
            "last_run_at",
            "next_run_at",
            "total_runs",
            "successful_runs",
            "failed_runs",
            "success_rate",
            "last_error_message",
            "created_at",
            "updated_at",
        ]

    def get_success_rate(self, obj):
        if obj.total_runs == 0:
            return 0

        return round((obj.successful_runs / obj.total_runs) * 100, 2)