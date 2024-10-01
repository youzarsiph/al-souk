""" URL Configuration for e_commerce """

from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your URLConf here.
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]