from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username','password','first_name','last_name','email']
    
    def validate_password(self,value):
        if not value:
            raise serializers.ValidationError('A senha é obrigatória')
        
        return value
    
    def validate_email(self,value):
        email = User.objects.filter(email=value)
        if not value:
            raise serializers.ValidationError('O e-mail é obrigatória')
        
        if email:
            raise serializers.ValidationError('Este e-mail já foi cadastrado')
        
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)