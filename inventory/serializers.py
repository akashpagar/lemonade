from rest_framework.serializers import ModelSerializer

from common.utils import ForcedResponse
from inventory.models import GlobalInventory


class GlobalInventorySerializer(ModelSerializer):
    class Meta:
        model = GlobalInventory
        fields = '__all__'

    def validate_item_name(self, value):
        if ' ' in value:
            raise ForcedResponse({'details': 'space not allowed in item name'})
        return value

    def validate(self, attrs):
        print(attrs, '>>>>>>>>>>>')
        return attrs

    # def create(self, validated_data):
    #     image_path = validated_data.get('image',None)
    #     if image_path:
