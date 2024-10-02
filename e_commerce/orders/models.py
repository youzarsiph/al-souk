"""
Order model

Represents an order.

Model Fields:
- user: Order owner
- status: Order status (pending, completed, cancelled)
- created_at: Date created
- updated_at: Last update

Relations with other models:
- User: One-to-many relationship with User model
"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Order(models.Model):
    """Orders"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Order owner",
    )
    status = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        help_text="Order status",
        choices=(
            (None, "Pending"),
            (True, "Completed"),
            (False, "Cancelled"),
        ),
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
        return f"Order {self.pk} by {self.user}"
