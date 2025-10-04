from rest_framework import serializers
from .models import Cliente, Certificado, ClienteCertificado

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'

class ClienteCertificadoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    certificado = CertificadoSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source="cliente", write_only=True
    )
    certificado_id = serializers.PrimaryKeyRelatedField(
        queryset=Certificado.objects.all(), source="certificado", write_only=True
    )

    
    class Meta:
        model = ClienteCertificado
        fields = [
            'id',
            'cliente',
            'certificado',
            'cliente_id',
            'certificado_id',
            'data_atribuicao',
        ]
    
    def get_cliente_nome(self, obj):
        return f"{obj.cliente.nome} {obj.cliente.apelido}"
    
    def get_certificado_titulo(self, obj):
        return obj.certificado.titulo