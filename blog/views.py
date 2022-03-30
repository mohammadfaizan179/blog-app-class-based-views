from django.contrib.auth import authenticate
from django.contrib.messages.api import success
from django.forms.fields import CharField
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.
from blog.models import Post
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from blog.forms import User_Signup, User_Login, PostForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UsernameField
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

#-------------------------------------------------
class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
#-------------------------------------------------
class ContactTemplateView(TemplateView):
    template_name = 'blog/contact.html'
#-------------------------------------------------
class UserSignupCreateView(CreateView):
    form_class = User_Signup
    template_name = 'blog/signup.html'
    success_url = '/signup/'                                 
#-------------------------------------------------
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        uname = user.username
        fname = user.first_name
        lname = user.last_name
        email = user.email
        groups = groups = user.groups.all()
        context = {
            'uname':uname,
            'fname':fname,
            'lname':lname,
            'email':email,
            'groups':groups,
        }
        return render(request,'blog/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')
#-------------------------------------------------
class UserLoginView(LoginView):
    template_name='blog/login.html'
    authentication_form=User_Login
#---------------------------------------------------------------------------------------
@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    template_name='blog/logout.html'
#-------------------------------------------------
class DashboardListView(ListView):
    model = Post
    template_name = 'blog/dashboard.html'
    context_object_name = 'posts'

    def get_context_date(self, request, *args, **kwargs):
        context = super().get_context_date(*args, **kwargs)
        context['full_name'] = self.context_object_name
#-------------------------------------------------
class PostAddCreateView(CreateView):
    form_class = PostForm
    template_name = 'blog/post_add.html'
    success_url = '/post-add/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
#-------------------------------------------------
class PostUpdateView(UpdateView):
    model =  Post
    form_class =  PostForm
    template_name = 'blog/post_update.html'
    success_url = '/dashboard/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
#-------------------------------------------------
@method_decorator(login_required, name='dispatch')
class PostDeletView(DeleteView):
    model = Post
    success_url = '/dashboard/'
#-------------------------------------------------
