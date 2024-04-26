from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean_verify_email(self):
        email = self.cleaned_data.get('email')
        vmail = self.cleaned_data.get('verify_email')

        if email and vmail and email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
        return vmail
