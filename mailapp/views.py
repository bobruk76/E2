from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from mailapp.models import Task
from mailapp.sendgrid_send_email import send_email, add_email_to_threading


class IndexPageView(TemplateView):
    template_name = 'index.html'

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    paginate_by = 10
    ordering = ['-created']

class TaskCreate(CreateView):
    model = Task
    fields = ['text', 'timer', 'to_email']
    # form_class = TaskSessionForm
    success_url = reverse_lazy('mailapp:task_list')
    template_name = '_edit.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        add_email_to_threading("vladimir.m.polyakov@gmail.com", task.to_email, task.text, task.timer)
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['text', 'timer', 'to_email']
    success_url = reverse_lazy('mailapp:task_list')
    template_name = '_edit.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        add_email_to_threading("vladimir.m.polyakov@gmail.com", task.to_email, task.text, task.timer)
        return super(TaskUpdate, self).form_valid(form)

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('mailapp:task_list')
    template_name = '_delete.html'