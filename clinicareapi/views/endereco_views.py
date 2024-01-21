from rest_framework.viewsets import ModelViewSet
from ..models import Endereco
from ..serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer 