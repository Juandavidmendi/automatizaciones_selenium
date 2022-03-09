import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest. TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_manejando_mouse(self):
		self.driver.get("https://www.mercadolibre.com.co")
		mouse_mov=self.driver.find_element_by_text("Categorias")

if __name__ == '__main__':
	unittest.main()