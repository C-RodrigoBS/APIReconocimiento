from attr import field
from rest_framework import serializers
from .models import Reconocimiento

class ReconocimientoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reconocimiento
        fields=('id','fotoReconocimiento','codigoReconocimiento','fechaHora')
        