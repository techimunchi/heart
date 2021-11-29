from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search_query_top")))
    driver.find_element(By.ID, "search_query_top").send_keys("dress", Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Printed Summer Dress']")))
    driver.find_element(By.XPATH, "//a[@href=http://automationpractice.com/index.php?id_product=5&controller=product&search_query=dress&results=7']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "color_11")))
    driver.find_element(By.ID, "color_11").click()
    driver.find_element(By.ID, "add_to_cart").click()