""" API endpoints for souk_al_furqan.reports """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from souk_al_furqan.reports.models import Report
from souk_al_furqan.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(ModelViewSet):
    """Create, read, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
