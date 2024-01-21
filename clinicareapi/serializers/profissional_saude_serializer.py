from rest_framework.serializers import ModelSerializer
from ..models import ProfissionalSaude,CustomUser
from .custom_user_serializers import CustomUserSerializer
from .endereco_serializers import EnderecoSerializer

class ProfissionalSaudeSerializer(ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = ['id','user_profissional','especialidade','conselho','numero_conselho','enderecos_atendimento']

    user_profissional = CustomUserSerializer(many=False)
    enderecos_atendimento = EnderecoSerializer(many=True)

    def create(self, validated_data):
        print('----------',validated_data)
        user_data  = validated_data.pop('user_profissional')
        enderecos_data = validated_data.pop('enderecos_atendimento',[])

        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save()

        profissional_saude_instance = ProfissionalSaude.objects.create(
            user_profissional=user_instance,
            **validated_data
        )

        for endereco in enderecos_data:
            profissional_saude_instance.enderecos_atendimento.create(**endereco)

        profissional_saude_instance.save()
        
        return profissional_saude_instance