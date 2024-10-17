""" Views for al_souk.orders """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from al_souk.mixins import OwnerMixin
from al_souk.orders.models import Order
from al_souk.orders.serializers import OrderSerializer
from al_souk.permissions import IsOwner


# Create your views here.
class OrderViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Orders"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    search_fields = ("name", "description")
    filterset_fields = ("status",)
    ordering_fields = ("status", "created_at", "updated_at")
