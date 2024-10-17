""" Views for al_souk.products """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from al_souk.products.models import Product
from al_souk.products.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    """Create, read, update and delete Products"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ("name", "description")
    filterset_fields = ("name", "price", "stock")
    ordering_fields = ("name", "created_at", "updated_at")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            self.permission_classes = (IsAuthenticated, IsAdminUser)

        else:
            self.permission_classes = (IsAuthenticated,)

        return super().get_permissions()
