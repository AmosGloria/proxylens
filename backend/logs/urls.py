from rest_framework.routers import DefaultRouter
from .views import RequestLogViewSet

router = DefaultRouter()
router.register(r"logs", RequestLogViewSet, basename="log")

urlpatterns = router.urls