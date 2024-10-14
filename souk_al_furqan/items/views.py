""" Views for souk_al_furqan.items """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from souk_al_furqan.items.models import Item
from souk_al_furqan.items.serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ModelViewSet):
    """Create, read, update and delete Order Items"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
