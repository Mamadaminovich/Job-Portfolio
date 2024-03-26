from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import *
from .models import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class User1ViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = User1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        name = request.data.get('name')
        password = request.data.get('password')

        if name and password:
            try:
                user = User1.objects.get(name=name, password=password)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            except User1.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Username or password is missing'}, status=status.HTTP_400_BAD_REQUEST)
        
def home(context):
    return render(context, "index.html", {})

