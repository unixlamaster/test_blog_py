from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=2048)
    create_date = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Post)
def send_email(sender, **kwargs):
    post = Post.objects.get(id=kwargs.get('instance').id)
    template = loader.get_template('post2email.html')
    subject = "Post in blog " + post.blog.user.username
    context = {  "header": post.header,
                 "text": post.text,
                 "id": post.id,
                 "host": getattr(settings, 'MY_DJANGO_URL_PATH', ''),
              }
    html_content = template.render(context)
    msg = EmailMultiAlternatives(subject, "", "", [post.user.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()    
    
class ReadPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)