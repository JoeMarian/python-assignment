from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]