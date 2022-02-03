import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.commochorn.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SeleniumMain:
    def __init__(self, driver):
        self.driver = driver

        self.browser_dictionary = {
            [["CHROME"], ["chrome", "google_chrome", "gc", "google"]],
            [["FIREFOX"], ["mozilla", "ff", "firefox", "mozilla_firefox", "mf"]],
            [["OPERA"], ["opera", "op"]],
            [["EDGE"], ["edge", "microsoft", "me", "microsoft_edge"]],
            [["EXPLORER"], ["explorer", "internet_explorer", "ie"]]
        }

    def open_browser(self, browser=None):
        if browser == None:
            driver = webdriver.Chrome()
        else:
            for i in range(len(self.browser_dictionary)):
                row = self.browser_dictionary.get(i)
                if browser in row[i][1]:
                    browser = row[i][0]
                    browser = browser.pop()
                    break
            if browser == "CHROME":
                driver = webdriver.Chrome()
            if browser == "OPERA":
                driver = webdriver.Opera()
            if browser == "FIREFOX":
                driver = webdriver.Firefox()
            if browser == "EDGE":
                driver = webdriver.Edge()
            if browser == "EXPLORER":
                driver = webdriver.Ie()

        driver.get(portal_url)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    def type_text_into_element(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def clear_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def switch_to_tab(self, tab):
        pass
