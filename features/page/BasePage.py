from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def _init_(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, keys):
        self.find_element(locator).send_keys(keys)

    def clear(self, locator):
        self.find_element(locator).clear()

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def wait_for_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))