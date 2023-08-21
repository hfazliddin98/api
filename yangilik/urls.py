from rest_framework.routers import SimpleRouter
from .views import YangilikViewSet



router = SimpleRouter()
router.register(r'yangilik', YangilikViewSet)


urlpatterns = router.urls