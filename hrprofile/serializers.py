from rest_framework import serializers
from signup.models import HRUser

class HRProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRUser
        fields = ['hr_name', 'email', 'phone', 'company_name']
        read_only_fields = ['email']
