from django.db import models
from projects.models import TargetURL


class ScrapingJob(models.Model):
    class Frequency(models.TextChoices):
        MANUAL = "manual", "Manual"
        HOURLY = "hourly", "Hourly"
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        FAILED = "failed", "Failed"

    class RunStatus(models.TextChoices):
        IDLE = "idle", "Idle"
        QUEUED = "queued", "Queued"
        RUNNING = "running", "Running"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    target_url = models.ForeignKey(
        TargetURL,
        on_delete=models.CASCADE,
        related_name="scraping_jobs"
    )
    name = models.CharField(max_length=255)

    frequency = models.CharField(
        max_length=20,
        choices=Frequency.choices,
        default=Frequency.MANUAL
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    run_status = models.CharField(
        max_length=20,
        choices=RunStatus.choices,
        default=RunStatus.IDLE
    )

    last_task_id = models.CharField(max_length=255, blank=True)

    last_run_at = models.DateTimeField(null=True, blank=True)
    next_run_at = models.DateTimeField(null=True, blank=True)

    total_runs = models.PositiveIntegerField(default=0)
    successful_runs = models.PositiveIntegerField(default=0)
    failed_runs = models.PositiveIntegerField(default=0)

    last_error_message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name