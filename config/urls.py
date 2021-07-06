from django.contrib import admin
from django.urls import path, include
from livrosbestsellers.views import LivrosViewSet
from livrosbestsellers.views import LivroTotalViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'livrosbestsellers', LivrosViewSet)
router.register(r'LivrosTotal', LivroTotalViewSet )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
