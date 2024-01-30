from rest_framework.viewsets import ModelViewSet
from ...serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        serializar = UserSerializer(
            instance=user,
            data=request.data,
            many=False,
            context={'request':request},
            partial=True
        )
        serializar.is_valid(raise_exception=True)
        serializar.save()
        return Response(serializar.data)
    
