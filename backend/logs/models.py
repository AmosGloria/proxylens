from django.db import models
from jobs.models import ScrapingJob
from projects.models import TargetURL


class RequestLog(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    job = models.ForeignKey(
        ScrapingJob,
        on_delete=models.CASCADE,
        related_name="request_logs"
    )
    target_url = models.ForeignKey(
        TargetURL,
        on_delete=models.CASCADE,
        related_name="request_logs"
    )
    url = models.URLField()
    status = models.CharField(max_length=20, choices=Status.choices)
    status_code = models.PositiveIntegerField(null=True, blank=True)
    response_time_ms = models.PositiveIntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    retry_count = models.PositiveIntegerField(default=0)
    response_size_bytes = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.url} - {self.status}"