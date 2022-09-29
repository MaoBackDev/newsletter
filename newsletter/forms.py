from django import forms

from .models import *


class NewsletterUserForm(forms.ModelForm):
    class Meta:
        model = NewsLetterUser
        fields = ['email']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'subject', 'body', 'email', 'status']