from rest_framework.viewsets import ModelViewSet
from ...serializers import ConsultaSerializer
from ...models import Consulta

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer