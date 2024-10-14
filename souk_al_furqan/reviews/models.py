"""
Review model

Represents a review for a product

Model Fields:
- user: User who wrote the review
- product: Product being reviewed
- rating: Rating given by the user
- content: Review content
- created_at: Date the review was created
- updated_at: Date the review was last updated

Relations with other models:
- User: One-to-many relationship with User model
- Product: One-to-many relationship with Product model
"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Review(models.Model):
    """Reviews"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Review owner",
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        help_text="Reviewed product",
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        help_text="Rating",
        choices=(
            (1, "1 Star"),
            (2, "2 Star"),
            (3, "3 Star"),
            (4, "4 Star"),
            (5, "5 Star"),
        ),
    )
    content = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        db_index=True,
        help_text="Review content",
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
        return f"{self.user} - {self.product}"
