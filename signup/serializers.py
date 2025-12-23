from rest_framework import serializers
from .models import HRUser

class HRSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRUser
        fields = ['hr_name', 'email', 'phone', 'company_name', 'password']
