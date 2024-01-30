from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from ...models import ProfissionalSaude
from ...serializers import ProfissionalSaudeSerializer

class ProfissionalSaudeViewSet(ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profissional = ProfissionalSaude.objects.filter(pk=pk).first()
        serializer = ProfissionalSaudeSerializer(
            instance=profissional,
            data=request.data,
            many=False,
            context={'request':request},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    