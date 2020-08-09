from django.urls import path

from teacher_app import views

app_name = 'teacher_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    # path('link/', views.link, name='link'),
    # path('add_content/', views.add_content, name='add_content'),
]
