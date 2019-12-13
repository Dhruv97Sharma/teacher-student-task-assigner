from django.urls import path,include
from django.conf.urls import include, url
from .views import Home, TaskView, AssignmentView
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views as user_views
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    UserTaskListView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('user/<str:username>', UserTaskListView.as_view(), name='user-tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    #path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='assignment_platform/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='assignment_platform/logout.html'), name='logout'),
    path('task/', TaskView.as_view(), name='task'),
	path('assign/', AssignmentView.as_view(), name='assign'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('assigntask/', user_views.assigntask, name='assigntask'),
]
