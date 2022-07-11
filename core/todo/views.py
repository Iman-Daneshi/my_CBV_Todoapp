from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Task
from .forms import PostForm
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'todo/index.html'

class TaskListView(ListView):
    context_object_name = 'tasks'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(CreateView):
    model = Task
    form_class = PostForm
    success_url = '/tasklist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = PostForm
    success_url = '/tasklist/'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/tasklist/'


