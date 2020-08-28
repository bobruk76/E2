from django.urls import path

from mailapp.views import TaskCreate, TaskList, IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view()),

    path('task/create', TaskCreate.as_view(), name='task_create'),
    path('tasts/', TaskList.as_view(), name='task_list'),
]
