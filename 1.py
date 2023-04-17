from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


requst = str(input("Введіть запит: "))
url = "https://www.google.com.ua/?hl=ru"

driver = webdriver.Chrome(executable_path="D:\\selenium\\chrome\\chromedriver.exe")

try:

    driver.get(url=url)
    element = driver.find_element(By.NAME,'q')
    element.send_keys(requst)

    element.submit()
    link = driver.find_element(By.TAG_NAME,'h3').click()
    
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()



   