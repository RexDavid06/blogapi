from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='Overview'),
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-detail/<int:pk>/', views.blogDetail, name='blog-detail'),
    path('blog-create/', views.blogCreate, name='blog-create'),
    path('blog-update/<int:pk>/', views.blogUpdate, name='blog-update'),
    # path('blog-delete/<int:pk>/', views.blogDelete, name='blog-delete'),
]