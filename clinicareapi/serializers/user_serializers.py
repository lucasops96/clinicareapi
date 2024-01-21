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

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)