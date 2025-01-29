from django.urls import path
from rest_framework.routers import SimpleRouter
from tyutor.views import TyutorProfilModelViewSet

router = SimpleRouter()
router.register(r'users', TyutorProfilModelViewSet)
# router.register(r'fakultets', FakultetsViewSet)


urlpatterns = []
urlpatterns += router.urls