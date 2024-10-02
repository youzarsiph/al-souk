""" Serializers for e_commerce.orders """

from rest_framework.serializers import ModelSerializer
from e_commerce.orders.models import Order


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
