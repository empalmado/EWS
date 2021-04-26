from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from EWS.views import Firstpage
from django.urls import resolve
#For Models testing
from EWS.models import Item

class IndexTest(TestCase):

	def html_index_root_mainpage_pwede_din_homepage_basta(self):
		found = resolve('/')
		self.assertEqual(found.func, Firstpage)

		
	def test_index_returns_correct_view(self):
		request = HttpRequest()
		response = Firstpage(request)
		html = response.content.decode('UTF-8')
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Mainpage.html')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertTemplateUsed(response, 'Mainpage.html')
		self.assertIn('<title>Empalmado Welding Shop</title>', html)
		self.assertIn('<h1 align="center">EWS Free Estimate</h1>', html)
		self.assertIn('<center>', html)
		self.assertIn('</center>', html)
		self.assertIn('<label id="Name">Name or Company Name:</label>', html)
		self.assertIn('<input type="text" id="Names" name="Name">', html)
		self.assertIn('<br>', html)
		self.assertIn('<label id="Contact">Contact No.:</label>', html)
		self.assertIn('<input type="text" id="Contacts" name="Contact">', html)
		self.assertIn('<label id="Iname">Product Name:</label>', html)
		self.assertIn('<input type="text" id="Inames" name="Iname">', html)
		self.assertIn('<label id="Size">Sizes of Product in inch/ft:</label>', html)
		self.assertIn('<input type="text" id="Sizes" name="Size">', html)
		self.assertIn('<label id="Type">Stainless Type 304 or 202:</label>', html)
		self.assertIn('<input type="text" id="Types" name="Type">', html)
		self.assertIn('<input type="submit" value="submit" id="Submits" name="Submit">', html)
		self.assertTrue(html.strip().endswith('</html>'))

class ORM_save_mo_na_teh(TestCase):
	def test_saving_koto(self):

		Item1 = Item()
		Item1.Name = 'Names'
		Item1.save()
		Item2 = Item()
		Item2.Contact = 'Contacts'
		Item2.save()
		Item3 = Item()
		Item3.ProductName = 'Inames'
		Item3.save()
		Item4 = Item()
		Item4.Size = 'Sizes'
		Item4.save()
		Item5 = Item()
		Item5.Type = 'Types'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(save1.Name, 'Names')
		self.assertEqual(save2.Contact, 'Contacts')
		self.assertEqual(save3.ProductName, 'Inames')
		self.assertEqual(save4.Size, 'Sizes')
		self.assertEqual(save5.Type, 'Types')

class ORM_save_mo_na_teh(TestCase):
	def test_saving_koto(self):

		Item1 = Item()
		Item1.Name = 'Names'
		Item1.save()
		Item2 = Item()
		Item2.Contact = 'Contacts'
		Item2.save()
		Item3 = Item()
		Item3.ProductName = 'Inames'
		Item3.save()
		Item4 = Item()
		Item4.Size = 'Sizes'
		Item4.save()
		Item5 = Item()
		Item5.Type = 'Types'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(save1.Name, 'Names')
		self.assertEqual(save2.Contact, 'Contacts')
		self.assertEqual(save3.ProductName, 'Inames')
		self.assertEqual(save4.Size, 'Sizes')
		self.assertEqual(save5.Type, 'Types')







# #from django.test import TestCase

# # Create your tests here.

# '''from django.urls import resolve
# from django.test import TestCase
# from EWS.views import MainPage


# from django.http import HttpRequest

# class HomePageTest(TestCase):
# 	def test_root_url_resolves_to_mainpage_view(self):
# 		found = resolve('/')
# 		self.assertEqual(found.func, MainPage)
	    	
# 	def test_mainpage_returns_correct_view(self):
# 		request = HttpRequest()
# 		response = MainPage(request)
# 		html = response.content.decode('utf8')
# 		self.assertTrue(html.startswith('<html>'))
# 		self.assertIn('<title>Empalmado Welding Shop</title>', html)
# 		self.assertTrue(html.endswith('</html>'))
# 		'''
	
# 	"""class ProjectDrin(TestCase):"""
	
# 	"""def test_root_url_resolves_to_mainpage_view(self):
# 		found = resolve('/')
# 		self.assertEqual(found.func, Mainpage)"""
