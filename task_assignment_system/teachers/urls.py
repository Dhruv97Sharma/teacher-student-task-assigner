from django.urls import path,include
from . import views as teachers_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', teachers_views.register, name='platform-teachers-register'),
    path('profile/', teachers_views.profile, name='platform-teachers-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='teachers/login.html'), name='platform-teachers-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='teachers/logout.html'), name='platform-teachers-logout'),
]
    