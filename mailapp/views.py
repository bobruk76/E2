from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from mailapp.models import Task

class IndexPageView(TemplateView):
    template_name = 'index.html'

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['text', 'timer']
    # form_class = TaskSessionForm
    success_url = reverse_lazy('mailapp:task_list')
    template_name = '_edit.html'

    def form_valid(self, form):
        model = form.save(commit=False)
        print(type(model))
        return super(TaskCreate, self).form_valid(form)
