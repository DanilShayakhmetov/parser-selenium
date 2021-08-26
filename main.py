# импорт библиотек
import os
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


chromedriver = "/usr/lib/chromium-browser/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://yandex.ru/news/smi")
content = driver.find_elements_by_css_selector('div.smi-chart__brick')
for i in content:
    time.sleep(2)
    i.click()
    back = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/form/button')
    time.sleep(5)
    back.click()

# content.click()
# print(content)





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
