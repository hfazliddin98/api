from rest_framework.routers import SimpleRouter
from .views import QabulArizaViewSet


router = SimpleRouter()
router.register(r'qabul_ariza', QabulArizaViewSet)



urlpatterns = router.urls