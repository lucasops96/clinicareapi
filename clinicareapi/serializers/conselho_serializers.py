from rest_framework.serializers import ModelSerializer
from ..models import Conselho

class ConselhoSerializer(ModelSerializer):
    class Meta :
        model = Conselho
        fields = ['nome']