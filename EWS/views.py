from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.
def Firstpage(request):

	if request.method == 'POST':

		Name = request.POST['Name']
		Contact = request.POST['Contact']
		ProductName = request.POST['Iname']
		Size = request.POST['Size']
		Type = request.POST['Type']
		
		
		rin = Item()
		rin.Name = Name
		rin.Contact = Contact
		rin.ProductName = ProductName
		rin.Size = Size
		rin.Type = Type
		rin.save()

	return render(request,'Mainpage.html')


def Page(request):
	rin = Item.objects.all().order_by('Name')
	return render(request,'Databasesu.html', {'rin': rin})