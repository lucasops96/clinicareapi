from rest_framework.viewsets import ModelViewSet
from ..serializers.paciente_serializers import PacienteSerializer
from ..models import Paciente
from rest_framework.response import Response

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        paciente = Paciente.objects.filter(pk=pk).first()
        serializer = PacienteSerializer(
            instance=paciente,
            data=request.data,
            many=False,
            context={'request':request},
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)