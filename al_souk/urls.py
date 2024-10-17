""" URL Configuration for al_souk """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from al_souk.categories.views import CategoryViewSet
from al_souk.items.views import ItemViewSet
from al_souk.orders.views import OrderViewSet
from al_souk.products.views import ProductViewSet
from al_souk.reports.views import ReportViewSet
from al_souk.reviews.views import ReviewViewSet
from al_souk.tags.views import TagViewSet


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
