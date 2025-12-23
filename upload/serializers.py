from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["id", "department", "uploaded_at", "resume_file", "parsed_skills"]
        read_only_fields = ["id", "uploaded_at", "parsed_skills"]
