from django.shortcuts import redirect, render, get_object_or_404
from .models import TodoModel
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
  todo_list = TodoModel.objects.all()
  template = "../templates/todo/list.html"
  # 検索機能
  keyword = request.GET.get('keyword')
  if keyword:
    result = todo_list.filter(
      # タイトル、本文で検索
      Q(title__icontains=keyword) |
      Q(body__icontains=keyword)
    )
    messages.success(request, '「{}」の検索結果'.format(keyword))
    # 検索にヒットしたもののみ表示
    return render(request, template, {'todo_list': result})
  return render(request, template, {'todo_list': todo_list})

#@login_required
def create(request):
  if request.method == "POST":
    copied = request.POST.copy()
    copied["user"] = request.user.id
    form = TodoForm(copied, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('todo_index')
  # GETメソッドでTodoForm呼び出し
  form = TodoForm
  return render(request, "todo/create.html", {'form': form})

def show(request, todo_id):
  todo = get_object_or_404(TodoModel, pk=todo_id)
#  user = Todo.user
  template = "todo/show.html"
  return render(request, template, {'todo': todo})

#@login_required
def update(request, todo_id):
  todo = get_object_or_404(TodoModel, pk=todo_id)
  template = "todo/update.html"
  if request.method == "POST":
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      return redirect('todo_index')
  form = TodoForm(instance=todo)
  return render(request, template, {'form': form, 'todo_id': todo_id})

#@login_required
def delete(request, todo_id):
  todo = get_object_or_404(TodoModel, pk=todo_id)
  todo.delete()
  return redirect('todo_index')