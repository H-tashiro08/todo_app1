from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm, TaskEditForm

class IndexView(View):
    def get(self, request):
        todo_list = Task.objects.all()
        context = {"todo_list": todo_list}
        return render(request, "mytodo/index.html", context)

index = IndexView.as_view()

class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, "mytodo/add.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "mytodo/add.html", {"form": form})

add = AddView.as_view()

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskEditForm(instance=task)

    return render(request, "mytodo/edit.html", {"form": form, "task": task})

def update_task_complete(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        task.complete = not task.complete
        task.save()
    return redirect("index")

def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect("index")
