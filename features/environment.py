from app.application import Application
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener


# Allure terminal commands:
# Run and save data:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature
# Get the results:
# allure serve test_results/


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Firefox(executable_path=r'C:\Users\brant\AppData\Local\Programs\Python\Python310\Scripts\geckodriver.exe')
    # context.driver = webdriver.Safari()

    ###############################################################################################################
    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("window-size=1700,1000")
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     executable_path='/Users/12-python-selenium-automation/chromedriver')
    ###############################################################################################################

    ###############################################################################################################
    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    ### for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())
    ###############################################################################################################

    ###############################################################################################################
    ## Browserstack ###
    desired_cap = {
        'bstack:options': {
            "osVersion": "10.0",
            "deviceName": "Samsung Galaxy S20",
            "appiumVersion": "1.22.0",
            "local": "false",
        },
        "browserName": "chrome",
    }

    #Register for BrowserStack, then grab below from https://www.browserstack.com/accounts/settings
    bs_user = 'aydinozturk_lT3Hv2'
    bs_key = 'Wk8FtqNhzPwpigKpx3gs'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    ###############################################################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
