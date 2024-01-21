from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from ..models import ProfissionalSaude
from ..serializers import ProfissionalSaudeSerializer

class ProfissionalSaudeViewSet(ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

    
    