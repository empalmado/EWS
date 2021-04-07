from selenium import webdriver
import unittest
#browser = webdriver.Firefox()#
#browser.get('http://127.0.0.1:8000')#

class EWS(unittest.TestCase):

	def setup(self):
	   self.browser = webdriver.firefox()
	   
	def tearDown(self):
	   self.browser.quit()
	   
	def test_browser_title(self):
	    self.browser.get('http://localhost:8000')
	    self.assertIn('EWS', self.browser.title)
	    self.fail('Finish the test NOW!')
	    
if __name__=='__main__':
	unittest.main()
