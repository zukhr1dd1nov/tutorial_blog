from django import forms
from django.core.exceptions import ValidationError
from main.models import ContactsModel


class ContactsModelForm(forms.ModelForm):

    def clean_phone(self):
        data = str(self.cleaned_data.get('phone'))
        if not data.isdecimal() and len(data)==12 :
            raise ValidationError('Только цифры!')
        return data

    class Meta:
        model = ContactsModel
        exclude = ['created_at']