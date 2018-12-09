from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.forms.models import model_to_dict
from django.views.generic.base import View
from django.views.generic.edit import FormView
import logging
from blogs.models import Blog, Post, ReadPost, Subscription
    
def index(request):
    logger = logging.getLogger(__name__)
    if request.user.is_authenticated:
        # Do something for authenticated users.
        template = loader.get_template('blogs.html')
        context = {
            'title': "Blogs",
            'bloglist': [blog.user.username for blog in Blog.objects.all()],
         }
    else:
        # Do something for anonymous users.
        context = {
            'title': "Login",
         }
        template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        
class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")