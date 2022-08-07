from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.index, name="todo_index"),
    path('create/', views.create, name="todo_create"),
    path('show/<int:todo_id>', views.show, name="todo_show"),
    path('update/<int:todo_id>', views.update, name="todo_update"),
    path('delete/<int:todo_id>', views.delete, name="todo_delete"),

]