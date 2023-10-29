from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = "post.html"
    model = Post
