# from rest_framework import serializers
# from .models import *

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)
#     description = serializers.CharField()
#     body = serializers.CharField()


from rest_framework import serializers
from .models import * 

# Lead Serializer
class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article 
    fields = '__all__'