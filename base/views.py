from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView,TemplateView
from . models import PostModel
from django.urls import reverse_lazy


class PostListView(ListView):
    model = PostModel
    template_name = "list.html"
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = PostModel
    template_name = "detail.html"
    context_object_name= 'post'
    fields = "__all__"

class PostUpdateView(UpdateView):
    model = PostModel
    template_name = "update.html"
    fields = ["title", "body",'done']


class PostDeleteView(DeleteView):
    model = PostModel
    template_name = "delete.html"
    success_url = reverse_lazy("list")