from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""MainPage = None"""

def MainPage(request):
	return HttpResponse('<html><title>Empalmado Welding Shop</title><h1 style="color:green;">EWS FREE ESTIMATION</h1> <form><label for="Iname">Item/Product Name:</label><br><input type="text" id="Iname" name="Iname" value=""><br><label for="Size">Size in inch/ft:</label><br><input type="text" id="Size" name="Size" value=""><br><br><input type="submit" value="Submit"></form> </body></html>')

