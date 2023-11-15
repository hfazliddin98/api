from rest_framework.routers import SimpleRouter
from .views import RahbariyatViewSet

router = SimpleRouter()
router.register(r'rahbariyat', RahbariyatViewSet)

urlpatterns = router.urls