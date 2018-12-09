from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
import logging
    
def index(request):
    logger = logging.getLogger(__name__)
    template = loader.get_template('blogs.html')
#    logger.error("--------------")
#    logger.error(request.user.is_authenticated)
    context = {
        'title': "Blogs",
        'bloglist': "Blog List",
     }
    return HttpResponse(template.render(context, request))
