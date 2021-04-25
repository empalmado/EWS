from django.db import models

class Item(models.Model):

	Name = models.CharField(max_length=50, null=True)
	Contact = models.CharField(max_length=50, null=True)
	ProductName = models.CharField(max_length=50, null=True)
	Size = models.CharField(max_length=50, null=True)
	Type = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.Name
















'''from django.db import models

# Create your models here.'''
