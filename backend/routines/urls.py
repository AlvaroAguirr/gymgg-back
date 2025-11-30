from rest_framework.routers import DefaultRouter
from .views import RoutinaViewSet, RoutineHistoryViewSet

router = DefaultRouter()

router.register(r'routines', RoutinaViewSet, basename='routines')
router.register(r'routine-history', RoutineHistoryViewSet, basename='routine-history')

urlpatterns = router.urls
