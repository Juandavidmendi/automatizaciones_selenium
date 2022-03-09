from selenium import webdriver
from time import sleep
  
driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.get("http://localhost/logistica/")
timeout = 10
  
''' Hacemos scroll complete en toda la página '''
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
sleep(10)
  
driver.quit()