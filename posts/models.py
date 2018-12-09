from django.db import models
from django.contrib.auth.models import User
import blogs

class Post(models.Model):
    blog = models.ForeignKey('blogs.Blog', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=2048)
    create_date = models.DateTimeField(auto_now=True)