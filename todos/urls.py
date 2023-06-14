from django.urls import path
from . import views

urlpatterns = [
    path('addtask',views.addtask,name="addtask"),
    path('mark_as_done/<int:id>/',views.mark_as_done,name="mark_as_done"),
    path('mark_as_undone/<int:id>/',views.mark_as_undone,name="mark_as_undone"),
    path('edit_task/<int:id>/',views.edit_task , name="edit_task"),
    path('delete_task/<int:id>/',views.delete_task , name="delete_task")
]