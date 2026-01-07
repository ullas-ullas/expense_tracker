from django.db import models

# Create your models here.

class Transaction(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
