from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    comment = models.TextField()
    location = models.CharField(max_length=100)
    nomber = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
