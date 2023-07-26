from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)

