from selenium import webdriver
import unittest


#browser = webdriver.Firefox()#
#browser.get('http://127.0.0.1:8000')#

#class EWS(unittest.TestCase):
class EWS(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	   
	#def tearDown(self):#
		#self.browser.quit()
		
	def test_browser__title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Empalmado Welding Shop', self.browser.title)
	    #self.fail('Finish the test NOW!')#
	    
if __name__=='__main__':
		unittest.main(warnings='ignore')
