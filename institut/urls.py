from rest_framework.routers import SimpleRouter
from .views import (
    Inistitut_kengashiViewSet, Institut_haqidaViewSet, Institut_tuzulmasiViewSet,
    QabulxonaViewSet, RekvizidlarViewSet
)


router = SimpleRouter()
router.register(r'kengash', Inistitut_kengashiViewSet)
router.register(r'haqida', Institut_haqidaViewSet)
router.register(r'tuzulma', Institut_tuzulmasiViewSet)
router.register(r'qabulxona', QabulxonaViewSet)
router.register(r'rekvizid', RekvizidlarViewSet)


urlpatterns = router.urls

