from rest_framework.routers import SimpleRouter
from .views import (
    Jamoatchlik_kengashiViewSet, Madaniyat_marifatViewSet, Oquv_uslubiyViewSet,
    Akademik_litseyViewSet, Ilmiy_faoliyatViewSet, Yoshlar_bilan_ishlashViewSet
)

router = SimpleRouter()
router.register(r'kengash', Jamoatchlik_kengashiViewSet)
router.register(r'madaniyat', Madaniyat_marifatViewSet)
router.register(r'uslubiy', Oquv_uslubiyViewSet)
router.register(r'akademik', Akademik_litseyViewSet)
router.register(r'faoliyat', Ilmiy_faoliyatViewSet)
router.register(r'yoshlar', Yoshlar_bilan_ishlashViewSet)

urlpatterns = router.urls