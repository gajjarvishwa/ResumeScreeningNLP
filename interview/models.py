from django.db import models

class Interview(models.Model):
    candidate_name = models.CharField(max_length=200)
    candidate_email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    mode = models.CharField(max_length=50)   # Online / Offline
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} - {self.date} {self.time}"
