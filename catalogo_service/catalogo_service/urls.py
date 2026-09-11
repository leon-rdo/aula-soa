from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # A API do serviço de Catálogo.
    path("api/", include("catalogo.urls")),
    # Login/logout da browsable API do DRF (canto superior direito).
    path("api-auth/", include("rest_framework.urls")),
    # O front da aula 1: servido pelo PRÓPRIO Django, de propósito.
    # Mesma origem => sem CORS. O CORS é assunto da aula 2, quando o
    # front sai daqui e passa a morar na porta 8080.
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
