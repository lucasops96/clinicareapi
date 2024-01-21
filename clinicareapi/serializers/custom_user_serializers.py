from rest_framework.serializers import ModelSerializer
from ..models import CustomUser, User
from .user_serializers import UserSerializer

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','user_custom','cpf','telefone','is_profissional_saude']
    
    user_custom = UserSerializer(many=False)


    def create(self, validated_data):
        user_data = validated_data.pop('user_custom')

        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save()
        
        custom_user_instance = CustomUser.objects.create(user_custom=user_instance, **validated_data)
        return custom_user_instance
