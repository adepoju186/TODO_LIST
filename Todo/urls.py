from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
       path('', views.task_list, name ='task_list'),
    path('register/',views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('task/<int:pk>/',views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'), 
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    ]