import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
class usando_unittest(unittest.TestCase):
	
	def setUp(self):
		chromeOptions=Options()
		chromeOptions.add_experimenta_option("prefs",{
		"download.default_directory" : "C:\dchrome",
			})
		self.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe", chrome_options=chromeOptions)

	def test_descargando_archivos(self):
		driver = self.driver
		driver.get()