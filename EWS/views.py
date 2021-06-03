from django.shortcuts import redirect, render
from .models import Item, User

# Create your views here.
def Firstpage(request):

	if request.method == 'POST':


		clients = User.objects.create()
		Item.objects.create(
			Name = request.POST['Name'],
			Email = request.POST['Email'],
			# Contact = request.POST['Contact'], 
			# ProductName = request.POST['Iname'],
			# Size = request.POST['Size'], 
			# Type = request.POST['Type'],
			 )
		return redirect('Paps')
		
		rin = Item()
		rin.Name = Name
		rin.Email = Email
		# rin.Contact = Contact
		# rin.ProductName = ProductName
		# rin.Size = Size
		# rin.Type = Type
		rin.save()

	return render(request,'Mainpage.html')


def Page(request):
	rin = Item.objects.all().order_by('Name')
	rin = Item.objects.all().order_by('Email')
	# rin = Item.objects.all().order_by('Contact')
	# rin = Item.objects.all().order_by('ProductName')
	# rin = Item.objects.all().order_by('Size')
	# rin = Item.objects.all().order_by('Type')

	return render(request,'Databasesu.html', {'rin': rin})

