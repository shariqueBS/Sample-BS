from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set up the webdriver (ensure the path to chromedriver is correct)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://www.google.com/")
print(driver.title)

# Option 1: Find the 'Sign in' button and click it (Google's 'Sign in' button has a unique class)
try:
    sign_in_button = driver.find_element(By.XPATH, "//a[@href='https://accounts.google.com/ServiceLogin']")
    sign_in_button.click()
except Exception as e:
    print(f"Error: {e}")

# Allow some time for the page to load (optional, use WebDriverWait for better handling)
driver.implicitly_wait(5)

# Optionally: Print the current title after the sign-in page loads
print(driver.title)

# Quit the driver after a short delay

