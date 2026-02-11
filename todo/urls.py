from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListListView.as_view(), name='list-list'),
    path('list/<int:pk>/', views.TodoListDetailView.as_view(), name='list-detail'),
    path('list/create/', views.TodoListCreateView.as_view(), name='list-create'),
    path('list/<int:pk>/task/create/', views.TaskCreateView.as_view(), name='task-create'),
]
