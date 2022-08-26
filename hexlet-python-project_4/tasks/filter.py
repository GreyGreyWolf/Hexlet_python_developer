import django_filters
from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['assigned_to', 'tags', 'status']
