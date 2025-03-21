from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # This should match the root of /tasks/
    path('create/', views.task_create, name='task_create'),
    path('<int:id>/edit/', views.task_update, name='task_update'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
]