from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from .models import *
from .serializers import ArticleSerializer

class ArticleView(APIView):

	permission_classes = [
		permissions.IsAuthenticated,
	]
	serializer_class = ArticleSerializer

	def get(self, request):
		articles = self.request.user.authors.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response({"articles": serializer.data})
	




# class LeadViewSet(viewsets.ModelViewSet):
# 	permission_classes = [
# 		permissions.IsAuthenticated,
# 	]
# 	serializer_class = LeadSerializer

# 	def get_queryset(self):
# 		return self.request.user.leads.all()

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)