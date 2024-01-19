from rest_framework.viewsets import ModelViewSet
from ..serializers.paciente_serializers import PacienteSerializer
from ..models import Paciente

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer