"""
Tag model

Represents a product tag

Model Fields:
- name: Product name
- description: Product description
- created_at: Date created
- updated_at: Last update
"""

from django.db import models


# Create your models here.
class Tag(models.Model):
    """Product Tags"""

    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Tag name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Tag description",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )

    def __str__(self) -> str:
        return self.name
