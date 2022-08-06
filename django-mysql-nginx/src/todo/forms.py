from django import forms
from .models import TodoModel


class NoteForm(forms.ModelForm):
  class Meta:
    model = TodoModel
    field = ('title', 'memo')
    widgets = {
      'memo': forms.Textarea(attrs={'rows': 10, 'cols': 50})
    }