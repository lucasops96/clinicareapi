from rest_framework.serializers import ModelSerializer
from ..models import Consulta

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id','paciente','profissional_saude','data_hora',
                  'descricao','local_atendimento']
    