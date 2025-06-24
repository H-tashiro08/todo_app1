# mytodo/urls.py
from django.urls import path
from mytodo import views as mytodo
from . import views


urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"),
    path("edit_task/<int:task_id>/", views.edit_task, name="edit_task"),  # 編集
    path("delete_task/", views.delete_task, name="delete_task"),
    path("update_task_complete/", views.update_task_complete, name="update_task_complete"),  # 完了状態の更新
]