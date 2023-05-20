import uuid

from django.db import models

from main.mixins import BaseModel


class Supplier(BaseModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    # TODO: Contact
    # TODO: Soft delete feature

    def __str__(self):
        return self.name
