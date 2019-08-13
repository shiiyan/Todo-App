from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('login', views.myloginpage, name='login'),
    path('loginuser', views.login_user, name='loginuser'),
    path('logoutuser', views.logout_user, name='logoutuser'),
    path('', views.index, name='index'),
    path('addtodolist', views.addTodolist, name='addtodolist'),
    path('addtodo/<int:todolist_id>/', views.addTodo, name='addtodo'),
    path('detail/<int:todolist_id>/', views.detail, name='detail'),
    path('complete/<int:todolist_id>/<int:todo_id>/', views.completeTodo, name='complete'),
    path('uncomplete/<int:todolist_id>/<int:todo_id>/', views.uncompleteTodo, name='uncomplete'),
    path('search', views.searchpage, name='searchpage'),
    path('result', views.result, name='searchresult'),
    path('deletetodolist/<int:todolist_id>/', views.deleteTodolist, name='deletetodolist'),
    path('deletecompleted/<int:todolist_id>/', views.deletecompleted, name='deletecompleted'),
    # path('accounts/', include('django.contrib.auth.urls')),
    
]
