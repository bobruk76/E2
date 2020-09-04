from django.urls import path

from mailapp.views import TaskCreate, TaskList, IndexPageView, TaskUpdate, TaskDelete

app_name = 'mailapp'
urlpatterns = [
    path('', IndexPageView.as_view()),

    path('task/create', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('task/', TaskList.as_view(), name='task_list'),
]
