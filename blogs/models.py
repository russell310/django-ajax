from django.db import models

# Create your models here.


class Blog(models.Model):
	name = models.CharField(max_length = 100)
	img = models.ImageField(upload_to = 'blog', blank = True, null = True)
	description = models.TextField()

	def __str__(self):
		return self.name


class Comment(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return self.name