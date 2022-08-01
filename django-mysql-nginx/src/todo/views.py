from django.shortcuts import redirect, render, get_object_or_404
from .models import TodoModel
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

def show(request, Todo_id):
  Todo = get_object_or_404(Todo, pk=Todo_id)
#  user = Todo.user
  template = "Todo/show.html"
  return render(request, template, {'Todo': Todo})

@login_required
def create(request):
  if request.method == "POST":
    copied = request.POST.copy()
    copied["user"] = request.user.id
    form = TodoForm(copied, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('Todo_index')
  # GETメソッドでTodoForm呼び出し
  form = TodoForm
  return render(request, "Todo/create.html", {'form': form})

@login_required
def update(request, Todo_id):
  Todo = get_object_or_404(Todo, pk=Todo_id)
  template = "Todo/update.html"
  if request.method == "POST":
    form = TodoForm(request.POST, instance=Todo)
    if form.is_valid():
      form.save()
      return redirect('Todo_index')
  form = TodoForm(instance=Todo)
  return render(request, template, {'form': form, 'Todo_id': Todo_id})

@login_required
def delete(request, Todo_id):
  Todo = get_object_or_404(Todo, pk=Todo_id)
  Todo.delete()
  return redirect('Todo_index')