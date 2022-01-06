from rest_framework.serializers import ModelSerializer

from . import models
from .models import items


class itemsSerializers(ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'
