""" API endpoints for souk_al_furqan.reviews """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from souk_al_furqan.reviews.models import Review
from souk_al_furqan.reviews.serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(ModelViewSet):
    """Create, read, update and delete Reviews"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
