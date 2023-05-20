"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from inventory.views import inventory_list_view, inventory_retrive_view
from main.regex import UUID_REGEX
from main.views import index, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("", index, name="index"),
    # TODO: temparaory
    path("logout/", logout_view, name="logout"),
    path("inventory/", inventory_list_view, name="inventory_list_view"),
    re_path(
        f"^inventory/(?P<inventory_id>{UUID_REGEX})/$",
        inventory_retrive_view,
        name="inventory_retrive_view",
    ),
    path("api/", include("api.urls", namespace="all")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
