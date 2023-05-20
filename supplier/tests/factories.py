import factory

from supplier.models import Supplier


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Sequence(lambda n: f"Test Supplier {n}")
