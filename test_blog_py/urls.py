from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', views.index),
    path('subscribe/', views.subscribe),
    path('unsubscribe/', views.unsubscribe),
    path('post/', views.post),
    path('blogpost/', views.blogpost),
    path('readpost/', views.readpost),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', RedirectView.as_view(url='/blogs/', permanent=True)),
] 