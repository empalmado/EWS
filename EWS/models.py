from django.db import models

class User(models.Model):

	FirstName = models.CharField(max_length=50, null=True)
	LastName = models.CharField(max_length=50, null=True)
	Email = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.Name

class Item(models.Model):

	clients = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	BuyProduct = models.CharField(max_length=50, null=True)
	FreeQuote = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Name

class QuotePage(models.Model):

	clients = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
	#Quotation
	CompanyName = models.CharField(max_length=50, null=True)
	Contact = models.CharField(max_length=50, null=True)
	Address = models.CharField(max_length=50, null=True)
	Date = models.CharField(max_length=50, null=True)


# 	def __str__(self):
# 		return self.Name


# class QuotePage2(models.Model):

	# clients = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	Gmail = models.CharField(max_length=50, null=True)
	ProductDes = models.CharField(max_length=50, null=True)
	MaterialsDescription = models.CharField(max_length=50, null=True)
	Quantity = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.Name

class BuyPage(models.Model):

	clients = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

	ProductName = models.CharField(max_length=50, null=True)
	Quantity = models.CharField(max_length=50, null=True)
	Contact = models.CharField(max_length=50, null=True)
	Address = models.CharField(max_length=50, null=True)
	Email = models.CharField(max_length=50, null=True)
	Payment = models.CharField('1','Cod'),('2','Gcash Mastercard')

	
	def __str__(self):
		return self.Name