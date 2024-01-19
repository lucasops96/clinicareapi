from rest_framework.serializers import ModelSerializer
from ..models import CustomUser
from .user_serializers import UserSerializer

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','user_custom','cpf','telefone','is_profissional_saude']
    
    user_custom = UserSerializer(many=False,source='user')

