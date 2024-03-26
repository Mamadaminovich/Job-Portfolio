from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import User1

class User1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ['name', 'last', 'password', 'email', 'contact']
