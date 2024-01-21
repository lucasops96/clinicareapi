from rest_framework.serializers import ModelSerializer
from ..models import Paciente,Endereco
from .custom_user_serializers import CustomUserSerializer
from .endereco_serializers import EnderecoSerializer

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','user_paciente','idade','peso','sexo','endereco']
    
    user_paciente = CustomUserSerializer(many=False)
    endereco = EnderecoSerializer(many=False)

    def create(self, validated_data):
        user_data = validated_data.pop('user_paciente')
        endereco_data = validated_data.pop('endereco', None)

        user_serializer = CustomUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save()

        endereco_instance = None
        if endereco_data:
            endereco_serializer = EnderecoSerializer(data=endereco_data)
            endereco_serializer.is_valid(raise_exception=True)
            endereco_instance = endereco_serializer.save()


        paciente_instance = Paciente.objects.create(
            user_paciente=user_instance,
            endereco=endereco_instance,
            **validated_data
        )
        
        paciente_instance.save()

        return paciente_instance