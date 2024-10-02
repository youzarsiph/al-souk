"""
Item model

Represents an item in an order.

Model Fields:
- order: Order
- product: Product
- quantity: Item quantity
- created_at: Date created
- updated_at: Last update

Relations with other models:
- Order: One-to-one relationship with Order model
- Product: One-to-one relationship with Product model
"""

from django.db import models


# Create your models here.
class Item(models.Model):
    """Order Items"""

    order = models.OneToOneField(
        "orders.Order",
        on_delete=models.CASCADE,
        help_text="Order",
    )
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        help_text="Product",
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        help_text="Quantity",
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
        return f"{self.product.name} ({self.quantity})"
