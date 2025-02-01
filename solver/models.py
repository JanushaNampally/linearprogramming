from django.db import models

# Create your models here.
class linearprogramminginput(models.Model):
    method = models.CharField(max_length=50)
    equations = models.TextField()
    solution = models.JSONField(null=True, blank=True)

