from django.urls import path
from rest_framework.routers import SimpleRouter
from tyutor.views import TyutorProfilModelViewSet, TopshiriqViewSet

router = SimpleRouter()
router.register(r'users', TyutorProfilModelViewSet)
router.register(r'topshiriq', TopshiriqViewSet)


urlpatterns = []
urlpatterns += router.urls