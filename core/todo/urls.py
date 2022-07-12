from django.urls import path
from .views import TaskListView, IndexTemplateView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskComplete

app_name = 'todo'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('tasklist/', TaskListView.as_view(), name='tasklist'),
    path('newtask/', TaskCreateView.as_view(), name='newtask'),
    path('edittask/<int:pk>', TaskUpdateView.as_view(), name='updatetask'),
    path('deletetask/<int:pk>', TaskDeleteView.as_view(), name='deletetask'),
    path('taskdone/<int:pk>', TaskComplete.as_view(), name='taskdone'),

]
