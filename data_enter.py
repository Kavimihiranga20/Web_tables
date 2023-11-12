import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/webtables")
driver.maximize_window()


def select_need_rows():
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    pagination = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pagination-bottom")))
    row_selector = pagination.find_element(By.TAG_NAME, "select")
    time.sleep(3)
    row_selector.click()
    time.sleep(3)
    row_selector.find_elements(By.TAG_NAME, "option")[0].click()
    row_selector.click()


