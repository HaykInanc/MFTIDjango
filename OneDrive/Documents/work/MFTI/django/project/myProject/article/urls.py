from django.urls import path
from .views import *


urlpatterns = [
    path('articles/', ArticleView.as_view()),
]