""" Serializers for souk_al_furqan.products """

from rest_framework.serializers import ModelSerializer
from souk_al_furqan.products.models import Product


# Create your serializers here.
class ProductSerializer(ModelSerializer):
    """Serialize bots"""

    class Meta:
        """Meta data"""

        model = Product
        fields = (
            "id",
            "url",
            "image",
            "name",
            "description",
            "price",
            "stock",
            "created_at",
            "updated_at",
        )
