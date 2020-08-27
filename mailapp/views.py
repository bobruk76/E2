from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from mailapp.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'reader_list.html'

class TaskCreate(CreateView):
    model = Task
    # form_class = ReaderSessionForm
    # success_url = reverse_lazy('p_library:reader_list')
    template_name = '_edit.html'