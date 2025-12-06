from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet, StockViewSet  # <-- Добавь эту строку

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [path('test/', views.test_view)] + router.urls

