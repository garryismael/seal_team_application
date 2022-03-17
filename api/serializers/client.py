from rest_framework.serializers import ModelSerializer
from api.models.client import Client

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'adresse')