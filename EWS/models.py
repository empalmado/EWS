from django.db import models

class EstimatePage(models.Model):

	clients = models.ForeignKey(EstimatePage, default=None, on_delete=models.CASCADE, null=True)
	#Quotation
	Name = models.CharField(max_length=50, null=True)
	Contact = models.CharField(max_length=50, null=True)
	Gmail = models.CharField(max_length=50, null=True)
	Date = models.CharField(max_length=50, null=True)
	Address = models.CharField(max_length=50, null=True)
	ProductDes = models.CharField(max_length=50, null=True)
	MaterialsDes = models.CharField(max_length=50, null=True)
	Quantity = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Name

class BuyPage(models.Model):

	clients = models.ForeignKey(BuyPage, default=None, on_delete=models.CASCADE, null=True)

	ProductName = models.CharField(max_length=50, null=True)
	Quantity = models.CharField(max_length=50, null=True)
	Contact = models.CharField(max_length=50, null=True)
	Gmail = models.CharField(max_length=50, null=True)
	Address = models.CharField(max_length=50, null=True)
	Payment = models.CharField('1','Cod')

	
	def __str__(self):
		return self.Name