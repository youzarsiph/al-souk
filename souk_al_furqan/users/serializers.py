""" Serializers for souk_al_furqan.users """

from rest_framework.serializers import ModelSerializer
from souk_al_furqan.users.models import User


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """Tag Serializer"""

    class Meta:
        """Meta data"""

        model = User
        fields = ("id", "url", "username", "first_name", "last_name")
