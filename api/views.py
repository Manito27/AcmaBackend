from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from .models import (Cliente, Certificado, ClienteCertificado)
from .serializers import (ClienteSerializer, CertificadoSerializer, ClienteCertificadoSerializer)


# ===========================
# CLIENTES
# ===========================
class ClientesAPIView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


    def get(self, request):
        clientes = self.queryset.all()
        serializer = self.serializer_class(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


    def get(self, request, pk):
        cliente = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cliente = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = get_object_or_404(self.queryset, pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===========================
# CERTIFICADOS
# ===========================
class CertificadosAPIView(generics.ListCreateAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    parser_classes = [MultiPartParser, FormParser] 

    def get(self, request):
        certificados = self.queryset.all()
        serializer = self.serializer_class(certificados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificadoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        cert = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cert)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cert = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(cert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cert = get_object_or_404(self.queryset, pk=pk)
        cert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ===========================
# CLIENTE ↔ CERTIFICADO
# ===========================
class ClienteCertificadosAPIView(generics.ListCreateAPIView):
    queryset = ClienteCertificado.objects.all()
    serializer_class = ClienteCertificadoSerializer
    permission_classes = [AllowAny]


    def get(self, request):
        relacoes = self.queryset.all()
        serializer = self.serializer_class(relacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteCertificadoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClienteCertificado.objects.all()
    serializer_class = ClienteCertificadoSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        relacao = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(relacao)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        relacao = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(relacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        relacao = get_object_or_404(self.queryset, pk=pk)
        relacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
