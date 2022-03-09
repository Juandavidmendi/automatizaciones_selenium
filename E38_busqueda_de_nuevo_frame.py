import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):

	def  setUp(self):
		self.driver = webdriver.Chrome("C:\dchrome\chromedriver.exe")

	def test_buscar_frame(self):
		driver = self.driver
		driver.get("http://www.google.com")
		driver.maximize_window()
		time.sleep(3)
		click1 = driver.find_element(By.ID, "gbwa")
		time.sleep(2)
		click1.click()
		time.sleep(2) 
		driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[3]/iframe"))
		time.sleep(3)
		click2 = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div/span")
		time.sleep(2)
		click2.click()
		time.sleep(5)
		click3 = driver.find_element(By.CSS_SELECTOR,"#dismissible")
		time.sleep(2)
		click3.click()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()