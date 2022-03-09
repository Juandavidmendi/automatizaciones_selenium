import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):

	def  setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_clickderecho(self):
		self.driver.get("https://www.selenium.dev/documentation/webdriver/understanding_the_components/")
		time.sleep(4)
		clickderecho = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/p[1]")
		actions = ActionChains(self.driver)	
		actions.context_click(clickderecho).perform()

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
		unittest.main()			