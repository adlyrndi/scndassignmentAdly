# from assignment-repository.todolist.views import show_todolist

from django.urls import path
from todolist.views import show_todolist
from todolist.views import register 
from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import logout_user 
from todolist.views import delete 
from todolist.views import update 
from todolist.views import create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('delete/<str:name>', delete, name='delete'),
    path('update/<str:name>', update, name='update'),   
    path('create_task/', create_task, name='create_task'),
]