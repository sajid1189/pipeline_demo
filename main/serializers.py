from rest_framework.serializers import ModelSerializer

from main.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer2(ModelSerializer):

    class Meta:
        model = Product
        fields = ("id",)


