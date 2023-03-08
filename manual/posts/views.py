from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404

from .models import Post, Group
from .forms import PostForm, EditForm


class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    ordering = ['-pub_date']


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


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
