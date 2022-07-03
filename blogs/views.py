from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogsModel

# Create your views here.

class BlogsView(ListView):
    model = BlogsModel
    template_name = 'main/blogs.html'
    paginate_by = 10

class BlogDetailView(DetailView):
    template_name = 'main/blogdetail.html'
    model = BlogsModel