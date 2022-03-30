
from blog import views
from django.urls import path
from django.contrib.auth import views as auth_views
from blog.forms import User_Login
urlpatterns = [
    path('', views.HomeListView.as_view(), name="home"),
    path('contact/', views.ContactTemplateView.as_view(), name="contact"),
    path('dashboard/', views.DashboardListView.as_view(), name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.UserSignupCreateView.as_view(), name="signup"),
    
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),

    path('post-add/', views.PostAddCreateView.as_view(), name="post_add"),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:pk>/', views.PostDeletView.as_view(), name="post_delete"),
]
