from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class TodoList(ListView):
  template_name = 'list.html'