from django.db import models
from django.contrib.auth.models import User


# Models For adding User Comntact Informations
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

