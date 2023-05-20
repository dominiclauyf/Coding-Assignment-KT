from rest_framework import serializers

from inventory.models import Inventory


class InventoryListSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name")

    class Meta:
        model = Inventory
        fields = ["id", "name", "supplier_name", "availability"]


class InventoryDetailSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name")

    class Meta:
        model = Inventory
        fields = "__all__"
