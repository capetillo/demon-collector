from django.forms import ModelForm
from .models import Soul

class SoulForm(ModelForm):
  class Meta:
    model = Soul
    fields = ['date', 'body']