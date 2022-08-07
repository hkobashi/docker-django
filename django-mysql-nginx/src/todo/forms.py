from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
  class Meta:
    model = TodoModel
    fields = ('title', 'memo')
    widgets = {
      'memo': forms.Textarea(attrs={'rows': 10, 'cols': 50})
    }