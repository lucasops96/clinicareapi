from rest_framework.serializers import ModelSerializer
from ..models import ProfissionalSaude
from .custom_user_serializers import CustomUserSerializer
from .endereco_serializers import EnderecoSerializer

class ProfissionalSaudeSerializer(ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = ['id','use_custom','especialidade','conselho','numero_conselho','enderecos_atendimento']

        use_custom = CustomUserSerializer(many=False,source='user')
        enderecos_atendimento = EnderecoSerializer(many=True)