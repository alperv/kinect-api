from django.db import models

class Images(models.Model):
    filepath = models.CharField(max_length=1000)
