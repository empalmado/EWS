from django.shortcuts import redirect, render
from .models import EstimatePage, BuyPage

# Create your views here.
def EstimatePage(request):

	if request.method == 'POST':


		clients = EstimatePage.objects.create()
		Item.objects.create(
			Name = request.POST['Name'],
			Contact = request.POST['Contact'], 
			Gmail = request.POST['Gmail'],
			Date = request.POST['Date'],
			Address = request.POST['Address'], 
			ProductDes = request.POST['ProductDes'],
			MaterialDes = request.POST['MaterialDes'],
			Quantity = request.POST['Quantity'],
			 )
		return redirect('Paps')

		clients = BuyPage.objects.create()
		Item.objects.create(
			ProductName = request.POST['Name'],
			Quantity = request.POST['Contact'], 
			Contact = request.POST['Gmail'],
			Gmail = request.POST['Date'],
			Address = request.POST['Address'], 
			 )
		return redirect('Paps')
		
	# 	rin = Item()
	# 	rin.Name = Name
	# 	rin.Contact = Contact
	# 	rin.Gmail = Gmail
	# 	rin.Date = Date
	# 	rin.Address = Address
	# 	rin.ProductDes = ProductDes
	# 	rin.MaterialDes = MaterialDes
	# 	rin.Quantity = Quantity
	# 	rin.save()

	# return render(request,'Estimate.html')




