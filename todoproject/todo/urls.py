from django.urls import path
from .views import task_list, task_create, CategoryList, CategoryCreate

urlpatterns = [
    path('tasks/', task_list, name='task-list'),              # FBV — GET список
    path('tasks/create/', task_create, name='task-create'),   # FBV — POST создать
    path('categories/', CategoryList.as_view(), name='cat-list'),     # CBV — GET
    path('categories/create/', CategoryCreate.as_view(), name='cat-create'),  # CBV — POST
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
