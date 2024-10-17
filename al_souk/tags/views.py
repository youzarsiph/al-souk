""" API endpoints for al_souk.tags """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from al_souk.tags.models import Tag
from al_souk.tags.serializers import TagSerializer


# Create your views here.
class TagViewSet(ModelViewSet):
    """Create, read, update and delete Tags"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ("name", "description")
    filterset_fields = ("name",)
    ordering_fields = ("name", "created_at", "updated_at")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = (IsAuthenticated, IsAdminUser)

        else:
            self.permission_classes = (IsAuthenticated,)

        return super().get_permissions()
