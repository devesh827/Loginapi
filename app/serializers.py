from rest_framework import serializers
from app.models import User
#create serializer here


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['username','password']