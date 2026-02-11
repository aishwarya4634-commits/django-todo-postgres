from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoList, Task


class TodoListListView(ListView):
    model = TodoList


class TodoListDetailView(DetailView):
    model = TodoList


class TodoListCreateView(CreateView):
    model = TodoList
    fields = ['name']
    success_url = reverse_lazy('list-list')


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']

    def form_valid(self, form):
        form.instance.todo_list_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list-detail', kwargs={'pk': self.kwargs['pk']})
