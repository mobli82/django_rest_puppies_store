from rest_framework import serializers
from .models import PuppyModel

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = PuppyModel
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')