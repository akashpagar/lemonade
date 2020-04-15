from rest_framework.serializers import ModelSerializer, RelatedField, ReadOnlyField

from productdetails.models import Task, Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    projtest = ProjectSerializer(source='ProjectRef', many=False)

    class Meta:
        model = Task
        fields = [
            'TaskID', 'TaskName', 'projtest',
        ]
