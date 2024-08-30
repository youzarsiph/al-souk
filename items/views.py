""" Views for e_commerce.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.items.models import Item
from e_commerce.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, read, update and delete Order Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = IsAuthenticated
