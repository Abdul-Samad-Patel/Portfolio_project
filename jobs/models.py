from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to ="images/")
    summaery = models.CharField(max_length=200)
