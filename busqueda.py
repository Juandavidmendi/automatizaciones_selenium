from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

palabra_busqueda = "sele"
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(5)

for i in range(1,11):
	elementos = driver.fnd_element_by_xpath("")