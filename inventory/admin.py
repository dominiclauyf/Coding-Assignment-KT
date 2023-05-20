from django.contrib import admin

from inventory.models import Inventory
from main.admin import CreatedUpdatedAtReadOnlyAdmin


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "stock", "availability", "supplier")
    readonly_fields = ["availability", *CreatedUpdatedAtReadOnlyAdmin.readonly_fields]


admin.site.register(Inventory, InventoryAdmin)
