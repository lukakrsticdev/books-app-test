from rest_framework import serializers
from .models import MyBooks

class MyBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBooks
        fields = ['id', 'name', 'description', 'image', 'created', 'updated', 'user']