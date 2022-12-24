from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='create'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='change'),
    path('', views.AllUsersView.as_view(), name='users'),
]