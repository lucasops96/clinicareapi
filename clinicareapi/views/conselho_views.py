from rest_framework.viewsets import ModelViewSet
from ..models import Conselho
from ..serializers import ConselhoSerializer

class ConselhoViewSet(ModelViewSet):
    queryset = Conselho.objects.all()
    serializer_class = ConselhoSerializer