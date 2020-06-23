from django.db import models

# Create your models here.
class notes(models.Model):
    notes = models.TextField()
    tags = models.CharField(max_length=100, null=True)



