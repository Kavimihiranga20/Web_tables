import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from faker import Faker

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
faker = Faker()

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


def form_fill():
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    age = faker.random_int(min=18, max=65)
    salary = faker.random_int(min=200000, max=600000)
    department = faker.random_element(elements=("IT", "HR", "Finance", "Marketing", "Operations"))

    driver.find_element(By.ID, "addNewRecordButton").click()
    form = driver.find_element(By.ID, "userForm")
    first_name_wrapper = form.find_element(By.ID, "firstName-wrapper")
    first_name_wrapper.find_element(By.TAG_NAME, "input").send_keys(first_name)
    last_name_wrapper = form.find_element(By.ID, "lastName-wrapper")
    last_name_wrapper.find_element(By.TAG_NAME, "input").send_keys(last_name)
    email_wrapper = form.find_element(By.ID, "userEmail-wrapper")
    email_wrapper.find_element(By.TAG_NAME, "input").send_keys(email)
    age_wrapper = form.find_element(By.ID, "age-wrapper")
    age_wrapper.find_element(By.TAG_NAME, "input").send_keys(age)
    salary_wrapper = form.find_element(By.ID, "salary-wrapper")
    salary_wrapper.find_element(By.TAG_NAME, "input").send_keys(salary)
    department_wrapper = form.find_element(By.ID, "department-wrapper")
    department_wrapper.find_element(By.TAG_NAME, "input").send_keys(department)

    driver.find_element(By.ID, "submit").click()


select_need_rows()
form_fill()
