from rest_framework.serializers import ModelSerializer
from ..models import ProfissionalSaude
from .custom_user_serializers import CustomUserSerializer
from .endereco_serializers import EnderecoSerializer

class ProfissionalSaudeSerializer(ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = ['id','user_profissional','especialidade','conselho','numero_conselho','enderecos_atendimento']

    user_profissional = CustomUserSerializer(many=False,source='user')
    enderecos_atendimento = EnderecoSerializer(many=True)