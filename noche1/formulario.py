from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5173")
name_input = driver.find_element(By.NAME,"nombre")
email_input = driver.find_element(By.NAME,"correo")

name_input.send_keys("Camila gonzales")
email_input.send_keys("Cami")

submit_btn = driver.find_element(By.XPATH , '//button[@type="submit"]')
submit_btn.click()

time.sleep(2)

success_msg = driver.find_element(By.CLASS_NAME,"mensaje-exito")
assert "Gracias por tu mensaje ."  in  success_msg.text

print("Test passed: Form submitted successfully.")
driver.quit()




