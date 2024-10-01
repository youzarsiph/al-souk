""" Views for e_commerce.products """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.products.models import Product
from e_commerce.products.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    """Create, read, update and delete Products"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
