from django.db.utils import IntegrityError
from django.test import TestCase

from inventory.models import Inventory
from inventory.tests.factories import InventoryFactory


class InventoryConstraintsTestCase(TestCase):
    def test_inventory_check_constraints_when_stock_is_zero(self):
        with self.assertRaises(IntegrityError):
            Inventory.objects.bulk_create(
                [InventoryFactory.build(stock=0, availability=True)]
            )

    def test_inventory_check_constraints_when_stock_gt_zero(self):
        with self.assertRaises(IntegrityError):
            Inventory.objects.bulk_create(
                [InventoryFactory.build(stock=1, availability=False)]
            )
