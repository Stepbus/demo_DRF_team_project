from django.urls import path

from admin_users_app import views

urlpatterns = [
    path('', views.register, name='register'),
]