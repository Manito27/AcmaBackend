from django.contrib import admin
from .models import (Cliente, Certificado, ClienteCertificado)


admin.site.register(Cliente)
admin.site.register(Certificado)
admin.site.register(ClienteCertificado)


