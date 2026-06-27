from rest_framework.routers import DefaultRouter
from .views import ScrapingJobViewSet

router = DefaultRouter()
router.register(r"jobs", ScrapingJobViewSet, basename="job")

urlpatterns = router.urls