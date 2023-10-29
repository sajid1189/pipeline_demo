from rest_framework.viewsets import ModelViewSet

from main.models import Product
from main.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


