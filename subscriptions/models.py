from django.db import models
from django.contrib.auth.models import User
import blogs

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    blog = models.ForeignKey('blogs.Blog', on_delete=models.DO_NOTHING)