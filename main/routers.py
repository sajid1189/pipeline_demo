from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet,basename="products")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
