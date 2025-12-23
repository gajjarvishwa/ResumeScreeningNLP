from django.db import models
from django.utils import timezone

class Resume(models.Model):
    # Candidate Info — added for real resume screening
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # Department or job role category
    department = models.CharField(max_length=100)

    # Upload and extraction data
    uploaded_at = models.DateTimeField(default=timezone.now)
    resume_file = models.FileField(upload_to='resumes/')
    parsed_text = models.TextField(null=True, blank=True)
    parsed_skills = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} — {self.id}"










class AcceptedCandidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume_file = models.CharField(max_length=500)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
