from django.urls import path

from mailapp.views import TaskCreate, TaskList, IndexPageView, TaskUpdate

app_name = 'mailapp'
urlpatterns = [
    path('', IndexPageView.as_view()),

    path('task/create', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/', TaskList.as_view(), name='task_list'),
]
