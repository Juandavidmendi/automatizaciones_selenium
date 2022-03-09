import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import webDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_inittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

	def test_usando_Explicit_wait(self):
		driver = self.driver
		driver.get("http://www.google.com")
		try:
			element = webDriverWait(driver, 10),until(
				EC.presence_of_element_located(By,NAME, "Q")
				)
		finally:
			driver.quit()

	if __name__ == '__main__':
		unittest.main()
