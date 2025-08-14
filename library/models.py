from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    


