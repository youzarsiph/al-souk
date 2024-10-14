"""
Report model

Represents 
"""

from django.db import models


REPORT_REASONS = (
    (0, "Rude or vulgar"),
    (1, "Harassment or hate speech"),
    (2, "Spam"),
    (3, "Copy right issue"),
    (4, "Inappropriate"),
    (5, "Other"),
)


# Create your models here.


class Report(models.Model):
    """Abuse Reports"""

    pass
