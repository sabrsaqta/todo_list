from django.db import models
from django.contrib.auth.models import User

# Категория задач
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Теги
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Кастомный менеджер для задач
class TaskManager(models.Manager):
    def completed(self):
        return self.filter(is_completed=True)

# Основная модель — Задача
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    # Кастомный менеджер
    objects = TaskManager()

    def __str__(self):
        return self.title
