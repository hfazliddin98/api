from rest_framework.routers import SimpleRouter
from .views import Talaba_nomiViewSet, Talaba_malumotViewSet, Talaba_bolimViewSet


router = SimpleRouter()
router.register(r'nomi', Talaba_nomiViewSet)
router.register(r'malumot', Talaba_malumotViewSet)
router.register(r'bolim', Talaba_bolimViewSet)


urlpatterns = router.urls