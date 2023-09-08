from django.db import models

# Create your models here.

class FormModel(models.Model):
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name