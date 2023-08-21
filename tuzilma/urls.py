from rest_framework.routers import SimpleRouter
from .views import YonalishViewSet, BolimViewSet, RahbarViewSet


router = SimpleRouter()
router.register(r'yonalish', YonalishViewSet)
router.register(r'bolim', BolimViewSet)
router.register(r'rahbar', RahbarViewSet)


urlpatterns = router.urls