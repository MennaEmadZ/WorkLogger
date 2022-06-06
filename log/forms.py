from django import forms
from .models import *
from django.forms import ModelForm

class LogHoursForm(ModelForm):
    date = forms.DateField(label="Date",required=True,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Log
        fields = ['duration', 'project', 'remarks', 'date']
    