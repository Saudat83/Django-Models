from django.apps import AppConfig
from django.contrib.auth import get_user_model 
from django.db import Post 
from django.db import models

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

class Post(models.Model):

# DB Fields
    Title =  title = models.CharField(max_length=200)
    Text = models.TextField("Any amount of text")
    Author = get_user_model("A Foreign Key to the current user model")
    Created_date = models.DateTimeField("A date-time column")
    Published_date = models.DateTimeField("A date-time column")