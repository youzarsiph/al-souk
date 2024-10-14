""" Views for souk_al_furqan.orders """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from souk_al_furqan.mixins import OwnerMixin
from souk_al_furqan.orders.models import Order
from souk_al_furqan.orders.serializers import OrderSerializer
from souk_al_furqan.permissions import IsOwner


# Create your views here.
class OrderViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Orders"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    search_fields = ("name", "description")
    filterset_fields = ("status",)
    ordering_fields = ("status", "created_at", "updated_at")
