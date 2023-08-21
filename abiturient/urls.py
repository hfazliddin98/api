from rest_framework.routers import SimpleRouter
from .views import Abiturient_nomiViewSet, Abiturient_bolimViewSet, Abiturient_malumotViewSet

router = SimpleRouter()
router.register(r'nomi', Abiturient_nomiViewSet)
router.register(r'bolim', Abiturient_bolimViewSet)
router.register(r'malumot', Abiturient_malumotViewSet)

urlpatterns = router.urls
