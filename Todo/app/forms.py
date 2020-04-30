from django import forms
from .models import List

class Listform(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
