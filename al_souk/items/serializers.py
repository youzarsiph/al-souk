""" Serializers for al_souk.items """

from rest_framework.serializers import ModelSerializer
from al_souk.items.models import Item


# Create your serializers here.
class ItemSerializer(ModelSerializer):
    """Serialize order items"""

    class Meta:
        """Meta data"""

        model = Item
        read_only_fields = ("order", "product")
        fields = (
            "id",
            "url",
            "order",
            "product",
            "quantity",
            "create_at",
            "updated_at",
        )
