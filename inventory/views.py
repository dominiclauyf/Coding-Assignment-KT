from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def inventory_list_view(request):
    return render(request, "inventory_list.html")


@login_required
def inventory_retrive_view(request, inventory_id):
    return render(request, "inventory_retrive.html", {"inventory_id": inventory_id})
