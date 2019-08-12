from django import forms
from .models import Neighbourhood,Profile,Business

class NewHoodForm(forms.ModelForm):
  class Meta:
    model=Neighbourhood
    fields='__all__'

  class NewProfileForm(forms.ModelForm):
    class Meta:
      model=Profile
      exclude=['user']
      
  class NewBusinessForm(forms.ModelForm):
    class Meta:
      model=Business
      exclude=['user']    