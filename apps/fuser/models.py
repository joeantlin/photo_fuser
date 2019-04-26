from __future__ import unicode_literals
from apps.log_app.models import User
from django.db import models

class Photo(models.Model):
    description = models.TextField()
    title       = models.CharField(max_length=45)
    image       = models.ImageField(max_length=255, upload_to="fullphoto/")
    imagethumb  = models.ImageField(max_length=255, upload_to="thumbphoto/")
    creator     = models.ForeignKey(User, related_name="photo", null=True, on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    comment     = models.TextField()
    photo       = models.ForeignKey(Photo, related_name="creatorcomment", null=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(User, related_name="usercomment", null=True, on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
