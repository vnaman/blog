from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from .views import (
    blogListView,
    blogDetailView,
    blogCreateView,
    blogUpdateView,

)
urlpatterns = [
    path('', views.home , name = 'blog-home'),
    path('blog/', blogListView.as_view() , name = 'blog-blog'),
    path('blog/<int:pk>/', blogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update', blogUpdateView.as_view(), name='blog-update'),
    path('blog/new/', blogCreateView.as_view(), name='blog-create'),
    path('register/', views.register , name = 'blog-register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),
    ]
