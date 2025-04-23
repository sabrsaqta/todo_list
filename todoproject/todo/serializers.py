from rest_framework import serializers
from .models import Task, Category, Tag

# === Ручной сериализатор (Serializer) ===
class SimpleTaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    is_completed = serializers.BooleanField()

# Еще один ручной — для тегов
class TagSerializerManual(serializers.Serializer):
    name = serializers.CharField()

# === Модельные сериализаторы (ModelSerializer) ===
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
