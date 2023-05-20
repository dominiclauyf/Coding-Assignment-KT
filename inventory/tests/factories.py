import factory
from factory import fuzzy

from inventory.models import Inventory


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inventory

    name = factory.Sequence(lambda n: "Test Inventory {}".format(n))
    stock = fuzzy.FuzzyInteger(0, 10)
    supplier = factory.SubFactory("supplier.tests.factories.SupplierFactory")
    availability = factory.LazyAttribute(lambda n: n.stock > 0)
    img = factory.django.ImageField(color="blue")
