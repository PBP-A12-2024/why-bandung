from django.db import models
import uuid 
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    last_modified = models.DateField(auto_now_add=True)
    description = models.TextField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1)

