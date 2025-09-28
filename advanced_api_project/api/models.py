from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
        return self.name

  class Meta:
        ordering = ['name']

class Book(models.Model):
  title = models.CharField(max_length=255)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

  def __str__(self):
        return self.title

  class Meta:
        ordering = ['title']

# Create your models here.
