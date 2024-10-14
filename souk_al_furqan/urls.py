""" URL Configuration for souk_al_furqan """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from souk_al_furqan.categories.views import CategoryViewSet
from souk_al_furqan.items.views import ItemViewSet
from souk_al_furqan.orders.views import OrderViewSet
from souk_al_furqan.products.views import ProductViewSet
from souk_al_furqan.reports.views import ReportViewSet
from souk_al_furqan.reviews.views import ReviewViewSet
from souk_al_furqan.tags.views import TagViewSet


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
