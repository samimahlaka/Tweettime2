from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    #id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/' , blank=True, null=True)
    #date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

