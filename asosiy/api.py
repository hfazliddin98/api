from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'fayl', views.FaylViewSet)