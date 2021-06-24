from rest_framework import serializers
from .models import VaccineRegisteraton

class VaccineRegisteratonSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineRegisteraton
        exclude = ('id','created_at',)

    
    def validate_new_password(self, value):
        if value:
            userExist = VaccineRegisteraton.objects.filter(mobile=value)
            if userExist:
                raise serializers.ValidationError('Mobile number is already registered')
            return value