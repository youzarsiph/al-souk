""" Serializers for souk_al_furqan.orders """

from rest_framework.serializers import ModelSerializer
from souk_al_furqan.orders.models import Order


# Create your serializers here.
class OrderSerializer(ModelSerializer):
    """Serialize orders"""

    class Meta:
        """Meta data"""

        model = Order
        read_only_fields = ("status",)
        fields = (
            "id",
            "url",
            "status",
            "created_at",
            "updated_at",
        )
