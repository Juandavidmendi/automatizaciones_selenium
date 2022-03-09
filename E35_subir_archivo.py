import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_subir_archivo(self):
		self.driver.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
		time.sleep(3)
		self.driver.find_element_by_id("customFile").send_keys("C:\\Users\juanc\OneDrive\Imágenes\carga larga.jpg")
		time.sleep(4)
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
			unittest.main()		
