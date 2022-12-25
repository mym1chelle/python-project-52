from django.urls import path
from task_manager.tasks import views


app_name = 'tasks'
urlpatterns = [
    path('', views.AllTasksView.as_view(), name='tasks'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='detail_view')
]
