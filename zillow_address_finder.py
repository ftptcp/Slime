import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# # Where is your ChromeDriver and Chrome Binary?
# driver_path = r"C:\Users\ftptc\aws\chromedriver-win64\chromedriver.exe"
# chrome_binary_path = r"C:\Users\ftptc\aws\chrome-win64\chrome.exe"
#
# # Set Chrome Options.
# # Tell the ChromeDriver to use the Chrome Binary (.exe) you specify
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = chrome_binary_path
#
# # Create your Chrome Service
# chrome_service = webdriver.ChromeService(executable_path=driver_path)

driver_path = r"C:\Users\ftptc\aws\chromedriver-win64\chromedriver.exe"
chrome_service2 = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=chrome_service2)


# Create the webdriver object to navigate the web-browser
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


def grabbing_the_cards(current_url):
    price_list = []

    driver.get(current_url)

    price_list = driver.find_elements(By.CLASS_NAME, "keSfom")
    for each_price in price_list:
        print(each_price.text)


def start():
    # # Get City and State from User
    # city = input("Enter City: ")
    # state = input("Enter State: ")

    # Visit zillow
    # zillow_url = r"https://www.zillow.com/"
    trulia_url = r"https://www.trulia.com/"
    driver.get(trulia_url)
    time.sleep(2)
    # Locate the search input element by its ID

    # ZILLOW CODE
    # search_input = driver.find_element(By.ID, "search-box-input")

    # TRULIA CODE
    search_input = driver.find_element(By.CLASS_NAME, "doCukb")

    # # User filter query
    # search_query = f"{city} {state}"
    search_query = "Alexandria Virginia"

    time.sleep(2)
    # Fill in the search input with your search query
    search_input.send_keys(search_query)

    time.sleep(2)
    search_input.send_keys(Keys.RETURN)

    time.sleep(5)

    # Function to work on the cards it grabs from the site (TRULIA)
    grabbing_the_cards(driver.current_url)
    # # # Press Enter to submit the form (assuming Enter key submission works)
    # # search_input.send_keys(Keys.RETURN)
    # submit_input_button = driver.find_element(By.CLASS_NAME, "bjkomQ")
    # submit_input_button.submit()
    #
    # time.sleep(3)
    # search_button = driver.find_element(By.CLASS_NAME, "bjkomQ")
    # search_button.send_keys(Keys.RETURN)

    time.sleep(15)


start()
