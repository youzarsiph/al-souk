""" API endpoints for e_commerce.reports """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from e_commerce.reports.models import Report
from e_commerce.reports.serializers import ReportSerializer


# Create your views here.
class ReportViewSet(ModelViewSet):
    """Create, read, update and delete Reports"""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)
