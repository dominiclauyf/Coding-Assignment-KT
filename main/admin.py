from django.contrib import admin


class CreatedUpdatedAtReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created",
        "modified",
    ]
