""" Serializers for souk_al_furqan.reports """

from rest_framework.serializers import ModelSerializer
from souk_al_furqan.reports.models import Report


# Create your serializers here.
class ReportSerializer(ModelSerializer):
    """Report Serializer"""

    class Meta:
        """Meta data"""

        model = Report
        fields = ("id", "url")
