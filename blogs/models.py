from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=2048)
    create_date = models.DateTimeField(auto_now=True)

class ReadPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)