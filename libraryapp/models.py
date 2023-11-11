from django.db import models

# Create your models here.

class bookdb(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    genre=models.CharField(max_length=100)
    Description=models.CharField(max_length=500)
    available_copies=models.IntegerField(null=True)


