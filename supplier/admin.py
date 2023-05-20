from django.contrib import admin

from main.admin import CreatedUpdatedAtReadOnlyAdmin
from supplier.models import Supplier

# Register your models here.
admin.site.register(Supplier, CreatedUpdatedAtReadOnlyAdmin)
