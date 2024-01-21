from rest_framework.serializers import ModelSerializer
from ..models import Paciente
from .custom_user_serializers import CustomUserSerializer
from .endereco_serializers import EnderecoSerializer

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','user_paciente','idade','peso','sexo','endereco']
    
    user_paciente = CustomUserSerializer(many=False)
    endereco = EnderecoSerializer(many=False)