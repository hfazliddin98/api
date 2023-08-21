from django.contrib import redirects
from rest_framework.routers import SimpleRouter
from .views import FaylViewSet

router = SimpleRouter()
router.register(r'api', FaylViewSet)


urlpatterns = router.urls