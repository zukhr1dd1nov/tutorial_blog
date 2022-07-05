from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from blogs.models import BlogsModel
from main.forms import ContactsModelForm
from main.models import ContactsModel

# Create your views here.
from works.models import WorksModel


class HomeView(ListView):
    template_name = 'main/home.html'

    def get_queryset(self):
        queryset = {
            'works': WorksModel.objects.order_by('-created_at')[:3],
            'blogs': BlogsModel.objects.order_by('-created_at')[:2]
        }
        return queryset

class ContactView(CreateView):
    template_name = 'main/contact.html'
    model = ContactsModel
    form_class = ContactsModelForm

    def post(self, request, *args, **kwargs):
        form = ContactsModelForm(data=self.request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')