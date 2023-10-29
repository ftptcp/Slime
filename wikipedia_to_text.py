import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\ftptc\aws\chromedriver-win64\chromedriver.exe"

chrome_service = webdriver.ChromeService(executable_path=driver_path)

driver = webdriver.Chrome(service=chrome_service)


def get_wkikitext(current_url, search_query):
    driver.get(current_url)

    html = driver.page_source
    # html = f"{html}"

    with open(f"{search_query}", "w") as my_file:
        for each in html:
            my_file.write(each)


def start():
    search_query = input("Wikipedia: ")
    wikipedia_url = r"https://www.wikipedia.org/"

    driver.get(wikipedia_url)
    time.sleep(1)

    search_input = driver.find_element(By.ID, value="searchInput")
    search_input.send_keys(search_query)

    search_input.send_keys(Keys.RETURN) # Simulate pressing ENTER
    time.sleep(2)

    get_wkikitext(driver.current_url, search_query)
    driver.quit()
start()