""" Serializers for e_commerce.tags """

from rest_framework.serializers import ModelSerializer
from e_commerce.tags.models import Tag


# Create your serializers here.
class TagSerializer(ModelSerializer):
    """Tag Serializer"""

    class Meta:
        """Meta data"""

        model = Tag
        fields = ("id", "url")
