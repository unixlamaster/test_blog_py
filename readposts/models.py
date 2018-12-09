from django.db import models
from django.contrib.auth.models import User
import posts

class ReadPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    post = models.ForeignKey('posts.Post', on_delete=models.DO_NOTHING)