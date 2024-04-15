from rest_framework import serializers
from AchieverAPI.models import Task, Subtask, Habit, HabitInstance, WeeklyGoal, UserSettings

class TaskSerializer(serializers.ModelSerializer):
    subtasks = serializers.SubtaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = [
            'id', 
            'is_done', 
            'title', 
            'description', 
            'difficulty', 
            'due_date', 
            'done_date', 
            'created_date',
            'subtasks'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
        }
        
class SubtaskSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(source='task.title')
    class Meta:
        model = Subtask
        fields = [
            'id',
            'is_done',
            'title',
            'description',
            'difficulty',
            'done_date',
            'created_date',
            'task'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
        }