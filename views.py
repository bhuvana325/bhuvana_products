from django.shortcuts import render

# Create your views here.
from .serializers import itemsSerializers
from .models import items
from rest_framework import status, permissions, generics, viewsets


# Create your views here.
class StudentCurd(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = items.objects.all()
    serializer_class = itemsSerializers
    # permission_classes = [permissions.AllowAny]
