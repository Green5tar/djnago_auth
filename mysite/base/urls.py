from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task_list')
]