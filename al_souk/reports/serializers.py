""" Serializers for al_souk.reports """

from rest_framework.serializers import ModelSerializer
from al_souk.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report Serializer"""

    class Meta:
        """Meta data"""

        model = Report
        fields = ("id", "url")
