from rest_framework.serializers import ModelSerializer
from ..models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields=['id','rua','numero','complemento','cidade','estado','cep','pais']
    