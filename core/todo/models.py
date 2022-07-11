from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    Description = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Description

    class Meta:
        ordering = ('-created_date',)
