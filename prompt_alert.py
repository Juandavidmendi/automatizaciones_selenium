from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/JUAN.MENDIVELSO/Desktop/ejemplos%20python%20selenium/prompt%20alert.html")
time.sleep(3)
alert = driver.find_element_by_name("prompt_alert")
alert.click()
time.sleep(3)
alert = driver.switch_alert()
alert.accept()
time.sleep(3)
diver.close
