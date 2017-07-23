from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")
    driver.maximize_window()
    return driver
