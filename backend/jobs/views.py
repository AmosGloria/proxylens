from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import ScrapingJob
from .serializers import ScrapingJobSerializer
from .services import run_scraping_job
from logs.serializers import RequestLogSerializer


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

        log = run_scraping_job(job)
        data = RequestLogSerializer(log).data

        return Response(
            {
                "message": "Job executed successfully.",
                "log": data,
            },
            status=status.HTTP_200_OK,
        )