from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("http://localhost:3000")
name_input = driver.find_element(By.Name,"nombre")
email_input = driver.find_element(By.Name,"correo")
name_input.send_keys("Camila gonzales")
email_input.send_keys("Cami")
submit_btn = driver.find_element(By.XPATH , '//button[@type="submit"]')
submit_btn.click()
time.sleep(2)
success_msg = driver.find_element(By.CLASS_NAME,"MENSAJE DE EXITO")
assert "Gracias por tu mensaje . "  in  succes_msg.text
driver.quit()




