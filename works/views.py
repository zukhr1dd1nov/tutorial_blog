from django.shortcuts import render
from django.views.generic import ListView, DetailView
from works.models import WorksModel

# Create your views here.

class WorksView(ListView):
    model = WorksModel
    template_name = 'main/works.html'
    paginate_by = 10

class WorkDetailView(DetailView):
    model = WorksModel
    template_name = 'main/workdetail.html'
