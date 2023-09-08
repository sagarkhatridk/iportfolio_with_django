from django import forms
from . models import FormModel
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = FormModel
        fields = ['name', 'Email', 'subject', 'message']