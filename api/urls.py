from django.urls import include, path
from rest_framework import routers

from inventory import api as inventory_api

app_name = "api"


router = routers.DefaultRouter()
router.register(r"inventory", inventory_api.InventoryViewSet, basename="inventory")

urlpatterns = [
    path("", include(router.urls)),
]
