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
from blogs.models import Blog, Post, ReadPost, Subscription
    
def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        template = loader.get_template('blogs.html')
        context = {
            'title': "Blogs",
            'bloglist': [{'id':b.id, 'name':b.user.username} for b in Blog.objects.all()],
			'subscriptions': [s.blog.id for s in Subscription.objects.filter(user=request.user)]
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("/login")

def subscribe(request):
    Subscription.objects.create(blog_id=request.GET['blog'],user=request.user)
    return HttpResponseRedirect("/blogs")
	
def unsubscribe(request):
    ReadPost.objects.filter(post__blog=request.GET['blog']).delete()
    Subscription.objects.filter(blog_id=request.GET['blog'],user=request.user).delete()
    return HttpResponseRedirect("/blogs")

def post(request):
    if request.method == 'GET':
        # Показываем форму для новго поста
        template = loader.get_template('new_post.html')
        context = {
            'title': "Новый пост",
         }
        return HttpResponse(template.render(context, request))
    else:
        # Добавляем новый пост
        Post.objects.create(blog=Blog.objects.filter(user=request.user)[0],user=request.user,header=request.POST['header'],text=request.POST['text'])
        return HttpResponseRedirect("/blogpost/")

def blogpost(request):
    template = loader.get_template('blogpost.html')
    context = {
        'title': "Лента новостей",
        'blogpost': [{'id':p.id, 'header':p.header, 'text':p.text, 'blogname':p.blog.user.username, 'date':p.create_date.strftime("%F %H:%M")} for p in Post.objects.filter(blog__subscription__user=request.user).order_by('-create_date')],
        'readpost': [p.post_id for p in ReadPost.objects.filter(user=request.user)],
    }
    return HttpResponse(template.render(context, request))

def readpost(request):
    ReadPost.objects.create(post_id=request.GET['post'],user=request.user)
    return HttpResponseRedirect("/blogpost")

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main.html"

    # В случае успеха перенаправим на главную.
    success_url = "/blogs"

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