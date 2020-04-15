from rest_framework.response import Response
from rest_framework.views import APIView
from pprint import pprint
from productdetails.models import Task
from productdetails.serializers import TaskSerializer


class GetTaskDetails(APIView):

    def get(self, request):
        q = Task.objects.filter(AssignedTo=2).select_related('ProjectRef')
        serializer = TaskSerializer(q, many=True)
        return Response(serializer.data)

    def put(self, request):
        q = Task.objects.filter(AssignedTo=2).select_related('ProjectRef')
        print(q.query)
        q.update(TaskName='update_name')
        return Response({'details':'ok'})
