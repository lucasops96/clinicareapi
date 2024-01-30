from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ...serializers import CustomUserSerializer
from ...models import CustomUser

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        custom_user = CustomUser.objects.filter(pk=pk).first()
        serializer = CustomUserSerializer(
            instance=custom_user,
            data=request.data,
            many=False,
            context={'request':request},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)