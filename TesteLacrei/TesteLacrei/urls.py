from django.contrib import admin
from django.urls import path, include
from appLacrei.views import ProfissionaisViewSet, ConsultasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profissionais', ProfissionaisViewSet, basename='Profissionais')
router.register('consultas', ConsultasViewSet, basename='Consultas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
