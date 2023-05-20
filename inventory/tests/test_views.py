from uuid import uuid4

from django.db.models import Q
from django.test import Client, TestCase
from django.urls import reverse

from api.tests.mixins import APITestCase, GetAPITestCaseMixin, ListAPITestCaseMixin
from inventory.models import Inventory
from inventory.serializers import InventoryDetailSerializer, InventoryListSerializer
from inventory.tests.factories import InventoryFactory
from user.tests.factories import UserFactory


class InventoryListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.url = reverse("inventory_list_view")

    def test_inventory_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "inventory_list.html")

    def test_inventory_list_view_when_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class InventoryRetriveViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.inventory = InventoryFactory()
        self.url = reverse(
            "inventory_retrive_view", kwargs={"inventory_id": self.inventory.id}
        )

    def test_inventory_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "inventory_retrive.html")

    def test_inventory_list_view_when_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class ListOrderViewSetTestCase(ListAPITestCaseMixin, APITestCase):
    list_url = reverse("all:inventory-list")
    list_url_string = "/api/inventory/"
    list_serializer_class = InventoryListSerializer

    def get_queryset(self):
        return Inventory.objects.all()

    def test_get_list(self):
        InventoryFactory.create_batch(3)

        queryset_result = self.get_queryset()

        self.assertEqual(queryset_result.count(), 3)
        self.assertListResponseEqual(queryset_result)

    def test_get_list_when_search(self):
        text = "abcdefg"
        InventoryFactory.create_batch(3)
        InventoryFactory(name=text)
        InventoryFactory(description=text)
        InventoryFactory(note=text)

        queryset_result = self.get_queryset().filter(
            Q(name__icontains=text)
            | Q(description__icontains=text)
            | Q(note__icontains=text)
        )

        self.assertEqual(queryset_result.count(), 3)

        self.assertListResponseEqual(queryset_result, filters={"search": text})

    def test_get_list_when_filter_by_name(self):
        text = "abcdefg"
        InventoryFactory.create_batch(3)
        InventoryFactory(name=text)

        queryset_result = self.get_queryset().filter(name=text)

        self.assertEqual(queryset_result.count(), 1)

        self.assertListResponseEqual(queryset_result, filters={"search": text})

    def test_get_list_when_filter_stock_number(self):
        InventoryFactory.create_batch(3, stock=5)
        InventoryFactory.create_batch(2, stock=10)
        InventoryFactory.create_batch(3, stock=15)

        queryset_result = self.get_queryset().filter(stock__gt=9)
        self.assertEqual(queryset_result.count(), 5)
        self.assertListResponseEqual(queryset_result, filters={"stock__gt": 9})

        queryset_result = self.get_queryset().filter(stock__lt=9)
        self.assertEqual(queryset_result.count(), 3)
        self.assertListResponseEqual(queryset_result, filters={"stock__lt": 9})

        queryset_result = self.get_queryset().filter(stock=2)
        self.assertEqual(queryset_result.count(), 0)
        self.assertListResponseEqual(queryset_result, filters={"stock": 2})


class RetrieveInventoryViewSetTestCase(GetAPITestCaseMixin, APITestCase):
    list_serializer_class = InventoryListSerializer
    get_serializer_class = InventoryDetailSerializer

    def setUp(self):
        super().setUp()

        self.get_instance = InventoryFactory()

        self.get_url = reverse(
            "all:inventory-detail", kwargs={"pk": str(self.get_instance.id)}
        )
        self.get_url_string = f"/api/inventory/{str(self.get_instance.id)}/"
        self.get_not_found_url = [
            reverse(
                "all:inventory-detail",
                kwargs={"pk": uuid4()},
            ),
        ]
