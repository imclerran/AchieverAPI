from django.db import models

# Create your models here.
class Task(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    difficulty = models.SmallIntegerField(default=1)
    due_date = models.DateTimeField(null=True, blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Subtask(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    difficulty = models.SmallIntegerField(default=1)
    done_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.title
    

class Habit(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    difficulty = models.SmallIntegerField(default=1)
    times_per_week = models.SmallIntegerField(default=7)
    skip_day_of_rest = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class HabitInstance(models.Model):
    date = models.DateField()
    is_done = models.BooleanField(default=False)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='habit_instances')

    def __str__(self):
        return self.habit.title + ' - ' + str(self.date)
    

class WeeklyGoal(models.Model):
    tasks = models.ManyToManyField(Task, related_name='weekly_goals')
    subtasks = models.ManyToManyField(Subtask, related_name='weekly_goals')
    first_day = models.DateField()
    last_day = models.DateField()

    def __str__(self):
        return 'Weekly Goal: ' + str(self.first_day) + ' - ' + str(self.last_day)
    

class UserSettings(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_day_of_week = models.SmallIntegerField(default=1)
    day_of_rest = models.SmallIntegerField(default=7)

    def __str__(self):
        return self.user.username + ' Settings'