from rest_framework.generics import ListCreateAPIView

from api.serializers.client import ClientSerializer, Client


class ClientListCreate(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer = ClientSerializer
