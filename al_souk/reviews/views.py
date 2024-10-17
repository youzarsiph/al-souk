""" API endpoints for al_souk.reviews """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from al_souk.reviews.models import Review
from al_souk.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(ModelViewSet):
    """Create, read, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
