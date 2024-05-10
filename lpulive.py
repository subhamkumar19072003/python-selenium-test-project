from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver_service = Service(executable_path=r"C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get("https://lpulive.lpu.in/login")

# Enter username
username_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputEmail")))
username_input.send_keys("12105022")

# Enter password
password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputPassword")))
password_input.send_keys("19072003Chang@")

# Click the login button
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-next')]")))
login_button.click()

# Wait for page to load
time.sleep(5)  # Adjust the time according to the page loading time

# Maximize the window
driver.maximize_window()

# Keep the window open
input("Press Enter to close the window...")

# Close the browser
driver.quit()
