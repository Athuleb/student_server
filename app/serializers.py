from rest_framework import serializers
from .models import studentDetails 

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentDetails
        fields = '__all__' 