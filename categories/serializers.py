""" Serializers for e_commerce.categories """

from rest_framework.serializers import ModelSerializer
from e_commerce.categories.models import Category


# Create your serializers here.
class CategorySerializer(ModelSerializer):
    """Category Serializer"""

    class Meta:
        """Meta data"""

        model = Category
        fields = [
            "id",
            "url",
            "name",
            "description",
            "product_count",
            "created_at",
            "updated_at",
        ]


class CategoryRetrieveSerializer(CategorySerializer):
    """Category Serializer"""

    class Meta(CategorySerializer.Meta):
        """Meta data"""

        depth = 1
        read_only_fields = ["products"]
        fields = CategorySerializer.Meta.fields + ["products"]
