from django.db import models


# Create your models here.
class Upload(models.Model):
    branch = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    date = models.DateField()
    file = models.FileField(upload_to='Files/')

