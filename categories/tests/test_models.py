""" Tests for e_commerce.categories.models """

from django.contrib.auth import get_user_model
from django.test import TestCase
from e_commerce.categories.models import Category
from e_commerce.products.models import Product


# Create your tests here.
User = get_user_model()


class CategoryTests(TestCase):
    """Category model tests"""

    def setUp(self) -> None:
        """Setup data"""

        # Product owner
        user = User(username="product_owner", email="user@example.com")
        user.save()
        self.user = user

        # Category
        category = Category(name="Test", description="Test Category")
        category.save()
        self.category = category

        # Product
        product = Product(
            category=category,
            user=user,
            title="Test",
            description="Test product",
        )
        product.save()
        self.product = product

        return super().setUp()

    def test_product_count(self):
        """Test for category.product_count"""

        self.assertEqual(self.category.product_count, 1)
