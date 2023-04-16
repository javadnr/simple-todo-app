from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView,TemplateView
from . models import PostModel


class PostListView(ListView):
    model = PostModel
    template_name = "list.html"
    context_object_name = 'posts'
