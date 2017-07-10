from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    return driver
