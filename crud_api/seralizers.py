from rest_framework import serializers
from .models import CrudUser

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudUser
        fields = ("__all__")