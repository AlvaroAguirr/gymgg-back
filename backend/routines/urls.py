from rest_framework.routers import DefaultRouter
from .views import RoutinaViewSet, RoutineHistoryViewSet,ExcerciseRecommendationViewSet,ExerciseViewSet

router = DefaultRouter()

router.register(r'routines', RoutinaViewSet, basename='routines')
router.register(r'routine-history', RoutineHistoryViewSet, basename='routine-history')
router.register(r'exercises-recommendation',ExcerciseRecommendationViewSet, basename='exercises-recomendation')

router.register(r'exercises', ExerciseViewSet, basename='exercises')



urlpatterns = router.urls
