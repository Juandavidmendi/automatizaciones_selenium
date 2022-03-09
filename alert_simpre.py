from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("file:///C:/Users/juanc/OneDrive/Documentos/ejemplos%20python%20selenium/alert_simpre.html")
time.sleep(5)
alerta_simple = driver.find_element_by_name("alert")
alerta_simple.click()
time.sleep(3)
alerta_simple = driver.switch_to.alert
alerta_simple.dismiss()
time.sleep(3)
driver.close()	