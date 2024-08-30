""" Views for e_commerce.orders """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.orders.models import Order
from e_commerce.orders.serializers import OrderSerializer


# Create your views here.
class OrderViewSet(ModelViewSet):
    """Create, read, update and delete Orders"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
