# импорт библиотек
import os

from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


chromedriver = "/usr/lib/chromium-browser/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")

# # путь к драйверу chrome
# chromedriver = '/usr/bin/chromium-browser'
# options = webdriver.ChromeOptions()
# options.add_argument('headless')  # для открытия headless-браузера
# browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get("https://yandex.ru/news/smi")







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
