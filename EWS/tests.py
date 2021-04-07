#from django.test import TestCase

# Create your tests here.

from django.urls import resolve
from django.test import TestCase
from EWS.views import Mainpage
class HomePageTest(TestCase):
	def test_root_url_resolves_to_mainpage_views(self):
		found=resolve('/')#
		self.asserEqual(found.func, MainPage)
		
#class ProjectDrin(TestCase):
	
	#def test_root_url_resolves_to_mainpage_view(self):
		#found = resolve('/')
		#self.assertEqual(found.func, Mainpage)
		
	#def test_mainpage_returns_correct_view(self):
		#request = HttpRequest()
		#responce = Mainpage(request)
		#html = responce.content.decode("utf8")
		#self.assertTrue(html.strip().startswith('<html>'))
		#self.assertIn('<title> Empalmado Welding Shop</title>' , html)
		#self.assertTrue(html.strip().endswitch(</html>))
		
	
	
