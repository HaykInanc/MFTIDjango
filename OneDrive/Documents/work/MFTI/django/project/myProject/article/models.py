from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
	user = models.ForeignKey(User, related_name ="authors", on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=255)
	email = models.EmailField()

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	body = models.TextField()
	author = models.ForeignKey('Author', 
								related_name='articles', 
								on_delete=models.CASCADE)

	def __str__(self):
		return self.title