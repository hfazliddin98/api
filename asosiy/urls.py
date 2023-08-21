from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include




schema_view = get_schema_view(
    openapi.Info(
        title="Qo`qon davlat pedagogika instituti",
        default_version='1.0.0',
        description="Qo`qon davlar pedagogika instituti sayti uchun ishlab chiqilgan",
        contact=openapi.Contact(email="hatamovfazliddin505@gmail.com"),
        license=openapi.License(name="KSPI License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)





urlpatterns = [
    path('haker/', admin.site.urls),
    path('v1/api-auth/', include('rest_framework.urls')),
    path('v1/', include('users.urls')),    
    path('v1/abiturient/', include('abiturient.urls')),
    path('v1/faoliyat/', include('faoliyat.urls')),
    path('v1/institut/', include('institut.urls')),
    path('v1/talaba/', include('talaba.urls')),
    path('v1/tuzilma/', include('tuzilma.urls')),
    path('v1/xizmat/', include('xizmat.urls')),
    path('v1/yangilik/', include('yangilik.urls')),
    path('v1/rest/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/rest/docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)