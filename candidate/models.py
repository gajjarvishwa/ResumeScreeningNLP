from django.db import models

class AcceptedCandidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume_file = models.CharField(max_length=300)
    score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
