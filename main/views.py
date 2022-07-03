from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from main.forms import ContactsModelForm
from main.models import ContactsModel

# Create your views here.



class HomeView(TemplateView):
    template_name = 'main/home.html'

class ContactView(CreateView):
    template_name = 'main/contact.html'
    model = ContactsModel
    form_class = ContactsModelForm

    def post(self, request, *args, **kwargs):
        form = ContactsModelForm(data=self.request.POST)
        if form.is_valid():
            print('dsfsf')
            form.save()
        return redirect('contact')
