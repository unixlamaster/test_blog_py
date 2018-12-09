from django.contrib import admin
from .models import Blog, Post, ReadPost, Subscription

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(ReadPost)
admin.site.register(Subscription)
