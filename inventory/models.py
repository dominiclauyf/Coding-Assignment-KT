import uuid

from django.db import models

from main.mixins import BaseModel


class Inventory(BaseModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    stock = models.PositiveIntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.PROTECT)
    img = models.ImageField()
    # TODO: Soft delete feature

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_availability_check",
                check=models.Q(stock__gt=0, availability=True)
                | models.Q(stock=0, availability=False),
            )
        ]

    def save(self, *args, **kwargs):
        self.availability = True if self.stock > 0 else False

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
