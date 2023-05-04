import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver:
    _instance = None

    def _new_(cls):
        if cls._instance is None:
            config = configparser.ConfigParser()
            config.read('ConfigurationData/conf.ini')
            browser = config['DEFAULT']['browser']
            cls.instance = super().new_(cls)
            cls._instance.driver = cls._get_driver(browser)
        return cls._instance

    @staticmethod
    def _get_driver(browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            return webdriver.Chrome(options=options)
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--start-maximized')
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f'Unsupported browser: {browser}')

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def close(self):
        self.driver.quit()
        self._instance = None