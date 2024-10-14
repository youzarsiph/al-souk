"""
Product model

Represents a product.

Model Fields:
- image: Product image
- name: Product name
- description: Product description
- price: Product price
- stock: Product stock
- created_at: Date created
- updated_at: Last update
"""

from django.db import models


# Create your models here.
class Product(models.Model):
    """Products"""

    image = models.ImageField(
        help_text="Product image",
        upload_to="images/products",
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Product name",
    )
    description = models.CharField(
        max_length=256,
        db_index=True,
        help_text="Product description",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product price",
    )
    stock = models.PositiveIntegerField(
        help_text="Product stock",
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
