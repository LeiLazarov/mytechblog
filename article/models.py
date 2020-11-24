from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)


class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=2000, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    views = models.IntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)


class Comment(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=255, null=True)
    article = models.ForeignKey(Article, related_name='comment', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)



