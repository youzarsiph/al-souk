"""
User model

Represents a user or customer.

Model Fields:
- username: Username.
- first_name: First name.
- last_name: Last name.
- email: Email address.
- image: Profile image.
- password: Password.
- is_staff: Whether the user is a staff member.
- is_active: Whether the user is active.
- is_superuser: Whether the user is a superuser.
- last_login: The last login date.
- date_joined: The date the user joined.
- groups: Permission groups.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Users (customers)"""

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/users/",
        help_text="User profile image",
    )
