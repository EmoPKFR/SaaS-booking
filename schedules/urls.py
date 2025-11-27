from rest_framework.routers import DefaultRouter
from .views import WorkingHoursViewSet

router = DefaultRouter()
router.register("working-hours", WorkingHoursViewSet, basename="working-hours")

urlpatterns = router.urls
