from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\ftptc\aws\chromedriver-win64\chromedriver.exe"
chrome_path = r"C:\Users\ftptc\aws\chrome-win64\chrome.exe"

# Options tells the driver where the Chrome binary is (.exe)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Create a chrome service
chrome_service = webdriver.ChromeService(executable_path=driver_path)

# Setup the driver object to control the Chrome Browser
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)



def real_time_price():
    user_input = input("Enter crypto: ")
    url = f"https://coinmarketcap.com/currencies/{user_input}"

    driver.get(url)
    price_tag = driver.find_element(By.CLASS_NAME, "dxubiK")

    print(price_tag.text)
    driver.quit()

real_time_price()
