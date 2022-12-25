from django.urls import path
from task_manager.statuses import views

app_name = 'statuses'
urlpatterns = [
    path('', views.AllStatusesView.as_view(), name='statuses'),
    path('create/', views.CreateStatusView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateStatusView.as_view(), name='change'),
    path('<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete')
]
