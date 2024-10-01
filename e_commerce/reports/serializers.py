""" Serializers for e_commerce.reports """

from rest_framework.serializers import ModelSerializer
from e_commerce.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report Serializer"""

    class Meta:
        """Meta data"""

        model = Report
        fields = ("id", "url")
