from django.urls import path

from . import views
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
