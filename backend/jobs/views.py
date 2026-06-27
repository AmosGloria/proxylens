from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import ScrapingJob
from .serializers import ScrapingJobSerializer
from .tasks import run_scraping_job_task


class ScrapingJobViewSet(viewsets.ModelViewSet):
    serializer_class = ScrapingJobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ScrapingJob.objects.filter(
            target_url__project__owner=self.request.user
        )

    def perform_create(self, serializer):
        target_url = serializer.validated_data.get("target_url")

        if target_url.project.owner != self.request.user:
            raise PermissionDenied("You do not have permission to create a job for this URL.")

        serializer.save()

    def perform_update(self, serializer):
        target_url = serializer.validated_data.get("target_url", serializer.instance.target_url)

        if target_url.project.owner != self.request.user:
            raise PermissionDenied("You do not have permission to update this job.")

        serializer.save()

    @action(detail=True, methods=["post"], url_path="run")
    def run(self, request, pk=None):
        job = self.get_object()

        if job.status != ScrapingJob.Status.ACTIVE:
            return Response(
                {
                    "message": "Only active jobs can be queued.",
                    "current_status": job.status,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if job.run_status in [
            ScrapingJob.RunStatus.QUEUED,
            ScrapingJob.RunStatus.RUNNING,
        ]:
            return Response(
                {
                    "message": "This job is already queued or running.",
                    "run_status": job.run_status,
                    "task_id": job.last_task_id,
                },
                status=status.HTTP_409_CONFLICT,
            )

        task = run_scraping_job_task.delay(job.id)

        job.run_status = ScrapingJob.RunStatus.QUEUED
        job.last_task_id = task.id
        job.last_error_message = ""
        job.save(update_fields=[
            "run_status",
            "last_task_id",
            "last_error_message",
            "updated_at",
        ])

        return Response(
            {
                "message": "Job queued successfully.",
                "job_id": job.id,
                "task_id": task.id,
                "run_status": job.run_status,
            },
            status=status.HTTP_202_ACCEPTED,
        )