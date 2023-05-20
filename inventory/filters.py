from django.db.models import Q
from django_filters import rest_framework as filters

from inventory.models import Inventory
from supplier.models import Supplier


class InventoryListFileter(filters.FilterSet):
    search = filters.CharFilter(method="filter_search")
    sort_by = filters.OrderingFilter(fields=(("created_at", "created"),))
    name = filters.CharFilter(lookup_expr="iexact")
    stock = filters.NumberFilter()
    stock__gt = filters.NumberFilter(field_name="stock", lookup_expr="gt")
    stock__lt = filters.NumberFilter(field_name="stock", lookup_expr="lt")
    supplier = filters.ModelChoiceFilter("supplier", queryset=Supplier.objects.all())

    class Meta:
        model = Inventory
        fields = ["sort_by", "search", "name", "availability", "stock", "supplier"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(note__icontains=value)
        )
