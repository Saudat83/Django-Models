from django.db import models
from .models import get_user_model 


# Create your models here.
from django.db import Post

class Post(models.Model):

# DB Fields
    Title =  title = models.CharField(max_length=200)
    Text = models.TextField("Any amount of text")
    Author = get_user_model("A Foreign Key to the current user model")
    Created_date = models.DateTimeField("A date-time column")
    Published_date = models.DateTimeField("A date-time column")
