from rest_framework import serializers

from .models import *

class mgserializer(serializers.ModelSerializer):
    class Meta:
        model=mg
        fields=('id','title','Description')
class ssserializer(serializers.ModelSerializer):
    class Meta:
        model=ss
        fields=('id','name','campgain')
