""" API endpoints for e_commerce.tags """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.tags.models import Tag
from e_commerce.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    """Create, read, update and delete Tags"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)
