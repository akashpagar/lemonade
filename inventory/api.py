from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from common.utils import ForcedResponse
from inventory.models import GlobalInventory
from inventory.serializers import GlobalInventorySerializer


class CreateItem(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GlobalInventory.objects
    serializer_class = GlobalInventorySerializer


class ListItem(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GlobalInventory.objects
    serializer_class = GlobalInventorySerializer


class RetrieveItem(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GlobalInventory.objects
    serializer_class = GlobalInventorySerializer
    lookup_field = 'item_name'

    def get(self, request, *args, **kwargs):
        try:
            item = GlobalInventory.objects.get(item_name=kwargs.get('item_name'))
        except GlobalInventory.DoesNotExist:
            raise ForcedResponse({'detail': 'not found'})
        serializer = GlobalInventorySerializer(item, many=False)
        return Response(serializer.data)


class DeleteItemAPI(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GlobalInventory.objects
    serializer_class = GlobalInventorySerializer
    lookup_field = 'item_name'

    def delete(self, request, *args, **kwargs):
        delete_type = request.query_params.get("delete_type", 'soft')
        instance = self.get_object()
        if delete_type == "hard":
            instance.delete()
        else:
            instance.deleted = True
            instance.save()
        return Response({"detail": "deleted"})


from rest_framework.viewsets import ViewSet