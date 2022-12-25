from django.urls import path
from task_manager.tasks import views


app_name = 'tasks'
urlpatterns = [
    path('', views.AllTasksView.as_view(), name='tasks'),
]
