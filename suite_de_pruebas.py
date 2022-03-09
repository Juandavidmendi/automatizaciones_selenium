import unittest 
from selenium import webdriver
import time

class suite(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_busqueda(Self):
		self.cdriver.get("https://google.com")
		self.busqueda = self.cdriver.find_element_by_name("q")
		self.busqueda.send_keys("selenium")	
		self.busqueda.submit()
		time.sleep(3)

	def tearDown(self):
		self.cdriver.quit()


if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output='resultados de mi test plan'))