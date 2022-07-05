from django import forms
from django.core.exceptions import ValidationError
from main.models import ContactsModel


class ContactsModelForm(forms.ModelForm):

    def clean_phone(self):
        data = str(self.cleaned_data.get('phone'))
        if not data[1:].isdecimal() and len(data)==13 :
            raise ValidationError('Только цифры!')
        return data

    class Meta:
        model = ContactsModel
        exclude = ['created_at']