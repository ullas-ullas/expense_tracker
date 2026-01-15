from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default = uuid.uuid4, editable= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


