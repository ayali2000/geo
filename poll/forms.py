from django.contrib.auth import forms
from django import forms
from . models import *

class Vote(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['Question','Name_1','Name_2','image_1','image_2']


 