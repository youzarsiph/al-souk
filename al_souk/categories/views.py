""" API endpoints for al_souk.categories """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from al_souk.categories.models import Category
from al_souk.categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    """Create, read, update and delete Categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
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
