from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('review/',views.review,name='review'),
    path('get_content/',views.get_content,name='get_content'),
    # path('get_content/',views.get_content,name='get_content')
    # path('add_content/', views.add_content, name='add_content'),
]
