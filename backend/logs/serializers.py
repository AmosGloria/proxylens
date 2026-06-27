from rest_framework import serializers
from .models import RequestLog


class RequestLogSerializer(serializers.ModelSerializer):
    job_name = serializers.CharField(source="job.name", read_only=True)
    target_url_value = serializers.CharField(source="target_url.url", read_only=True)
    project_name = serializers.CharField(source="target_url.project.name", read_only=True)

    class Meta:
        model = RequestLog
        fields = [
            "id",
            "job",
            "job_name",
            "target_url",
            "target_url_value",
            "project_name",
            "url",
            "status",
            "status_code",
            "response_time_ms",
            "error_message",
            "retry_count",
            "response_size_bytes",
            "created_at",
        ]
        read_only_fields = fields