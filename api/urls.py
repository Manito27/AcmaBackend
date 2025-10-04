from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Clientes
    path("clientes/", views.ClientesAPIView.as_view(), name="clientes-list-create"),
    path("clientes/<int:pk>/", views.ClienteAPIView.as_view(), name="cliente-detail"),

    # Certificados
    path("certificados/", views.CertificadosAPIView.as_view(), name="certificados-list-create"),
    path("certificados/<int:pk>/", views.CertificadoAPIView.as_view(), name="certificado-detail"),

    # Cliente ↔ Certificado
    path("cliente-certificados/", views.ClienteCertificadosAPIView.as_view(), name="cliente-certificados-list-create"),
    path("cliente-certificados/<int:pk>/", views.ClienteCertificadoAPIView.as_view(), name="cliente-certificado-detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)