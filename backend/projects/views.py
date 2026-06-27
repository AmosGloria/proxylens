from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Project, TargetURL
from .serializers import ProjectSerializer, TargetURLSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TargetURLViewSet(viewsets.ModelViewSet):
    serializer_class = TargetURLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TargetURL.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        project = serializer.validated_data.get("project")

        if project.owner != self.request.user:
            raise PermissionDenied("You do not have permission to add URLs to this project.")

        serializer.save()

    def perform_update(self, serializer):
        project = serializer.validated_data.get("project", serializer.instance.project)

        if project.owner != self.request.user:
            raise PermissionDenied("You do not have permission to update this URL.")

        serializer.save()