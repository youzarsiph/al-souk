""" API endpoints for al_souk.reports """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from al_souk.reports.models import Report
from al_souk.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(ModelViewSet):
    """Create, read, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
