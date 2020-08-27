from django.urls import path

from mailapp.views import TaskCreate, TaskList

urlpatterns = [
path('reader/create', TaskCreate.as_view(), name='reader_create'),
path('reader/', TaskList.as_view(), name='reader_list'),
]