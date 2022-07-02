from django import forms
from .models import todotable

class todoForm(forms.ModelForm):
 class Meta:
    model=todotable
    fields='__all__'