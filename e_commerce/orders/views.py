""" Views for e_commerce.orders """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.mixins import OwnerMixin
from e_commerce.orders.models import Order
from e_commerce.orders.serializers import OrderSerializer
from e_commerce.permissions import IsOwner


# Create your views here.
class OrderViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Orders"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    search_fields = ("name", "description")
    filterset_fields = ("status",)
    ordering_fields = ("status", "created_at", "updated_at")
