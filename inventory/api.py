from rest_framework import viewsets

from inventory.filters import InventoryListFileter
from inventory.models import Inventory
from inventory.serializers import InventoryDetailSerializer, InventoryListSerializer


class InventoryViewSet(viewsets.ReadOnlyModelViewSet):
    filterset_class = InventoryListFileter

    def get_queryset(self):
        return Inventory.objects.select_related("supplier")

    def get_serializer_class(self):
        if self.action == "list":
            return InventoryListSerializer
        return InventoryDetailSerializer
