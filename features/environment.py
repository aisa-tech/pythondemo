import allure
from selenium import webdriver

from utilities import configReader


def before_scenario(context, scenerio):
    print("Before scenerio executed")
    '''
    if configReader.readConfig("basic info", "browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if configReader.readConfig("basic info", "browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    '''

def after_scenario(context, scenerio):
    print("After scenerio executed")
    context.driver.quit()


def after_step(context, step):

    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)