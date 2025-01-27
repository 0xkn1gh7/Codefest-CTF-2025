from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def crawl_pages():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://127.0.0.1:5000/")
        print(f"Accessed: {driver.current_url}")

        if "Login" in driver.page_source:
            print("Login required. Logging in...")
            driver.get("http://127.0.0.1:5000/login")
            driver.find_element(By.NAME, "username").send_keys("admin")
            driver.find_element(By.NAME, "password").send_keys("tQ5GKZAY9g")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

        driver.get("http://127.0.0.1:5000/")
        articles = driver.find_elements(By.CLASS_NAME, "article-title")
        for article in articles:
            print(f"Found article: {article.text}")

        for article in articles:
            try:
                article.click()
                print(f"Visiting: {driver.current_url}")
                time.sleep(5) 
                driver.back()
            except:
                continue

    finally:
        driver.quit()
