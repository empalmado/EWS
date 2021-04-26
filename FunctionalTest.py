from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):

	
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Empalmado Welding Shop', self.browser.title)
		
		hder = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('EWS Free Estimate', hder)
		
		l1 = self.browser.find_element_by_id('Name').text
		self.assertIn('Name or Company Name:', l1)

		l2 = self.browser.find_element_by_id('Contact').text
		self.assertIn('Contact No.:', l2)

		l3 = self.browser.find_element_by_id('Iname').text
		self.assertIn('Product Name:', l3)

		l4 = self.browser.find_element_by_id('Size').text
		self.assertIn('Sizes of Product in inch/ft:', l4)

		l5 = self.browser.find_element_by_id('Type').text
		self.assertIn('Stainless Type 304 or 202:', l5)

		in1 = self.browser.find_element_by_id('Names')  
		in1 = self.browser.find_element_by_id('Names').send_keys("Aldrin Empalmado")
		time.sleep(2)

		in2 = self.browser.find_element_by_id('Contacts')  
		in2 = self.browser.find_element_by_id('Contacts').send_keys("09092116086")
		time.sleep(2)

		in3 = self.browser.find_element_by_id('Inames')  
		in3 = self.browser.find_element_by_id('Inames').send_keys("Griller")
		time.sleep(2)

		in4 = self.browser.find_element_by_id('Sizes')  
		in4 = self.browser.find_element_by_id('Sizes').send_keys("12inchx24inch")
		time.sleep(2)

		in5 = self.browser.find_element_by_id('Types')  
		in5 = self.browser.find_element_by_id('Types').send_keys("304")
		time.sleep(2)

		submitbutton = self.browser.find_element_by_name('Submit').click()
		time.sleep(2)


		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get('http://localhost:8000')
		
		in1 = self.browser.find_element_by_id('Names')  
		in1 = self.browser.find_element_by_id('Names').send_keys("Chef Boy")
		time.sleep(2)

		in2 = self.browser.find_element_by_id('Contacts')  
		in2 = self.browser.find_element_by_id('Contacts').send_keys("09352477689")
		time.sleep(2)

		in3 = self.browser.find_element_by_id('Inames')  
		in3 = self.browser.find_element_by_id('Inames').send_keys("Food Pan")
		time.sleep(2)

		in4 = self.browser.find_element_by_id('Sizes')  
		in4 = self.browser.find_element_by_id('Sizes').send_keys("12inchx8inch")
		time.sleep(2)

		in5 = self.browser.find_element_by_id('Types')  
		in5 = self.browser.find_element_by_id('Types').send_keys("202")
		time.sleep(2)

		submitbutton = self.browser.find_element_by_name('Submit').click()
		time.sleep(2)


		self.browser.quit()	
		self.browser = webdriver.Firefox()
		self.browser.get('http://localhost:8000')


if __name__ == '__main__':
	unittest.main()