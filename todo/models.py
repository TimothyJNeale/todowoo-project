from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# The model for the basic to do model
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)

    importance = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])  # Changed to IntegerField for priority levels  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
