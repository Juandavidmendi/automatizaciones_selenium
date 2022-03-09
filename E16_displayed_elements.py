from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)
displayelemen = driver.find_element_by_name("btnI")
print(displayelemen.is_displayed()) #regresa true or false si ya cargo el elemento
print(displayelemen.is_enabled())#tambien regresa un true or false si el elemento esta disponible 
