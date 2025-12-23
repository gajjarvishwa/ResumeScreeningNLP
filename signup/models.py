from django.db import models

class HRUser(models.Model):
    hr_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)  # hashed or plain (your choice)

    def __str__(self):
        return self.email
