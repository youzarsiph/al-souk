""" Views for al_souk.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from al_souk.items.models import Item
from al_souk.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, read, update and delete Order Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
