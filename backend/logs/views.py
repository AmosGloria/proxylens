from rest_framework import viewsets, permissions

from .models import RequestLog
from .serializers import RequestLogSerializer


class RequestLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RequestLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = RequestLog.objects.filter(
            target_url__project__owner=self.request.user
        )

        job_id = self.request.query_params.get("job")
        target_url_id = self.request.query_params.get("target_url")
        status_value = self.request.query_params.get("status")

        if job_id:
            queryset = queryset.filter(job_id=job_id)

        if target_url_id:
            queryset = queryset.filter(target_url_id=target_url_id)

        if status_value:
            queryset = queryset.filter(status=status_value)

        return queryset