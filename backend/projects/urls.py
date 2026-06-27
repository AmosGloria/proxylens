from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TargetURLViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"target-urls", TargetURLViewSet, basename="target-url")

urlpatterns = router.urls