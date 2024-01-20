from rest_framework.viewsets import ModelViewSet
from ..models import ProfissionalSaude
from ..serializers.profissional_saude_serializer import ProfissionalSaudeSerializer

class ProfissionalSaudeViewSet(ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer