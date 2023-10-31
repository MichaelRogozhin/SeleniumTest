from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

print("Тестирование начато.")

driver = webdriver.Firefox()

driver.get("http://www.google.com")

elem = driver.find_element(By.NAME, "q")
elem.send_keys("selenium")
elem.submit()

#пауза 5 сек.
sleep(5)

elem = driver.find_element(By.LINK_TEXT, "Ещё")
elem.click()

elem = driver.find_element(By.LINK_TEXT, "Картинки")
elem.click()

#пауза 5 сек.
sleep(5)

elem = driver.find_element(By.LINK_TEXT, "Все")
elem.click()


print("Тестирование завершено.")


