""" API endpoints for e_commerce.reviews """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.reviews.models import Review
from e_commerce.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(ModelViewSet):
    """Create, read, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
