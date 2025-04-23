from django.urls import path
from .views import (
    task_list,
    create_task,
    TaskDetailView,
    CategoryListView,
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path('tasks/', task_list, name='task-list'),                    # FBV — GET список задач
    path('tasks/create/', create_task, name='task-create'),         # FBV — POST новая задача
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),  # CBV — GET, PUT, DELETE

    path('categories/', CategoryListView.as_view(), name='cat-list'),       # CBV — GET категории

    path('login/', login_view, name='login'),                       # POST логин
    path('logout/', logout_view, name='logout'),                    # POST логаут
    path('register/', register_view, name='register'),              # POST регистрация
]
