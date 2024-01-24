from rest_framework.viewsets import ModelViewSet
from ..serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
