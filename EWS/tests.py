from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from EWS.views import Firstpage
from django.urls import resolve
#For Models testing
from EWS.models import Item, User

class IndexTest(TestCase):

	def test_html_index_root_mainpage(self):
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


		


class ListViewTest(TestCase):

	def test_uses_list_template(self):
		clients = User.objects.create()
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'Mainpage.html')
	def test_uses_home_template(self):
		response = self.client.get('/Paps/')
		self.assertTemplateUsed(response, 'Databasesu.html')
	def test_displays_all_list_items(self):
		clients = User.objects.create()
		Name = Item.objects.create(Name='Name')
		Contact = Item.objects.create(Contact='Contact')
		ProductName = Item.objects.create(ProductName='ProductName')
		Size = Item.objects.create(Size='Size')
		Type = Item.objects.create(Type='Type')
		response = self.client.get('/')
		self.assertIn('Name', response.content.decode())
		self.assertIn('Contact', response.content.decode())
		self.assertIn('Iname', response.content.decode())
		self.assertIn('Size', response.content.decode())
		self.assertIn('Type', response.content.decode())
		Name = Item.objects.get(Name="Name")
		Contact = Item.objects.get(Contact="Contact")
		ProductName = Item.objects.get(ProductName="ProductName")
		Size = Item.objects.get(Size="Size")
		Type = Item.objects.get(Type="Type")
		
		self.assertEqual(Item.objects.count(), 5)


class ORM_save(TestCase):
	def test_savin(self):

		Item1 = Item()
		Item1.Name = 'Aldrin Empalmado'
		Item1.save()
		Item2 = Item()
		Item2.Contact = '09092116086'
		Item2.save()
		Item3 = Item()
		Item3.ProductName = 'Griller'
		Item3.save()
		Item4 = Item()
		Item4.Size = '12inchx24inch'
		Item4.save()
		Item5 = Item()
		Item5.Type = '304'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(save1.Name, 'Aldrin Empalmado')
		self.assertEqual(save2.Contact, '09092116086')
		self.assertEqual(save3.ProductName, 'Griller')
		self.assertEqual(save4.Size, '12inchx24inch')
		self.assertEqual(save5.Type, '304')

class ORM_save_(TestCase):
	def test_savin(self):

		Item1 = Item()
		Item1.Name = 'Aldrin Empalmado'
		Item1.save()
		Item2 = Item()
		Item2.Contact = '09092116086'
		Item2.save()
		Item3 = Item()
		Item3.ProductName = 'Griller'
		Item3.save()
		Item4 = Item()
		Item4.Size = '12inchx24inch'
		Item4.save()
		Item5 = Item()
		Item5.Type = '304'
		Item5.save()
		saveall = Item.objects.all()
		self.assertEqual(saveall.count(), 5)
		save1 = saveall[0]
		save2 = saveall[1]
		save3 = saveall[2]
		save4 = saveall[3]
		save5 = saveall[4]
		self.assertEqual(save1.Name, 'Aldrin Empalmado')
		self.assertEqual(save2.Contact, '09092116086')
		self.assertEqual(save3.ProductName, 'Griller')
		self.assertEqual(save4.Size, '12inchx24inch')
		self.assertEqual(save5.Type, '304')


