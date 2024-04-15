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


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            'id',
            'title',
            'description',
            'difficulty',
            'times_per_week',
            'skip_day_of_rest',
            'created_date',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
        }


class HabitInstanceSerializer(serializers.ModelSerializer):
    habit = HabitSerializer()
    class Meta:
        model = HabitInstance
        fields = [
            'id',
            'date',
            'is_done',
            'habit',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'date': {'read_only': True},
        }


class WeeklyGoalSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    subtasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Subtask.objects.all())
    class Meta:
        model = WeeklyGoal
        fields = [
            'id',
            'tasks',
            'subtasks',
            'first_day',
            'last_day',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
        }


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            'id',
            'user',
            'first_day_of_week',
            'day_of_rest',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
        }