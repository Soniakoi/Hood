from django import forms
from .models import Neighbourhood,Profile,Business

class NewHoodForm(forms.ModelForm):
  class Meta:
    model=Neighbourhood
    fields='__all__'