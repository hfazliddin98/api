from rest_framework.routers import SimpleRouter
from .views import Talim_turiJadvalViewSet, FakultetJadvalViewSet, \
    YonalishJadvalViewSet, KursJadvalViewSet, JadvalViewSet


router = SimpleRouter()
router.register(r'talim_turi', Talim_turiJadvalViewSet)
router.register(r'fakultet', FakultetJadvalViewSet)
router.register(r'yonalish', YonalishJadvalViewSet)
router.register(r'kurs', KursJadvalViewSet)
router.register(r'jadval', JadvalViewSet)


urlpatterns = router.urls