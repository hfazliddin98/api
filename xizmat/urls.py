from rest_framework.routers import SimpleRouter
from .views import Interaktiv_xizmatlarViewSet


router = SimpleRouter()
router.register(r'xizmatlar', Interaktiv_xizmatlarViewSet)

urlpatterns = router.urls
