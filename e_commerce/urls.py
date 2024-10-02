""" URL Configuration for e_commerce """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from e_commerce.categories.views import CategoryViewSet
from e_commerce.items.views import ItemViewSet
from e_commerce.orders.views import OrderViewSet
from e_commerce.products.views import ProductViewSet
from e_commerce.reports.views import ReportViewSet
from e_commerce.reviews.views import ReviewViewSet
from e_commerce.tags.views import TagViewSet


# Create your URLConf here.
router = DefaultRouter()
router.register("categories", CategoryViewSet, "category")
router.register("items", ItemViewSet, "item")
router.register("orders", OrderViewSet, "order")
router.register("products", ProductViewSet, "product")
router.register("reports", ReportViewSet, "report")
router.register("reviews", ReviewViewSet, "review")
router.register("tags", TagViewSet, "tag")

urlpatterns = [
    path("", include(router.urls)),
]
