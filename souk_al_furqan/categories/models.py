"""
Category model

Represents a product category

Model Fields:
- name: Category name
- description: Category description
- updated_at: Last update
- created_at: Date created

Methods:
- product_count: Number of products of a category
"""

from django.db import models


# Create your models here.
class Category(models.Model):
    """Categories"""

    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Category Name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Category Description",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    @property
    def product_count(self) -> int:
        """Number of products of a category"""

        return self.products.count()

    def __str__(self) -> str:
        return self.name
