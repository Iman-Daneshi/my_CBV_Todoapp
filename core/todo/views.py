from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Task
from .forms import PostForm
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'todo/index.html'

class TaskListView(LoginRequiredMixin, ListView):
    context_object_name = 'tasks'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = PostForm
    success_url = '/tasklist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = PostForm
    success_url = '/tasklist/'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/tasklist/'

@login_required
def task_done_view(request, pk):
    task = Task.objects.get(id=pk)
    task.done = True
    task.save()
    return redirect('todo:tasklist')
