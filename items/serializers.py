""" Serializers for e_commerce.items """

from rest_framework.serializers import ModelSerializer
from e_commerce.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Serialize order items"""

    class Meta:
        """Meta data"""

        model = Item
        fields = ("id", "url")
