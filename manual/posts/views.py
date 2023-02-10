from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'posts/update_post.html'
