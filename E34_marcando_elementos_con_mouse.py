import unittest 
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_manejando_mouse(self):
		self.driver.get("https://nicolasalvarez.com")
		time.sleep(3)
		mouse_mov=self.driver.find_element_by_xpath("")
		mouse_mov2=self.driver.find_element_by_xpath("")
		movimiento=ActionChains(self.driver)
		movimiento.move_to_element(mouse_mov).move_to_element(mouse.mov2).click().perform()
		time.sleep(3)

	def tearDown(self):
		self.drive.close()
