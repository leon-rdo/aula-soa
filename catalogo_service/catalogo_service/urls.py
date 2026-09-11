from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # A API do serviço de Catálogo.
    path("api/", include("catalogo.urls")),
    # Login/logout da browsable API do DRF (canto superior direito).
    path("api-auth/", include("rest_framework.urls")),
]
