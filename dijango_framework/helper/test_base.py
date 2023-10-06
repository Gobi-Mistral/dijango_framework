import time
from datetime import datetime
import logging
import platform
import os
from pathlib import Path
from telnetlib import EC
from typing import Optional

from django.test import LiveServerTestCase
from appium import webdriver as appium_webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver as selenium_webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from dijango_framework.helper import env

current_os = platform.system()
logger = logging.getLogger(__name__)

class TestBase(LiveServerTestCase):
    def __init__(self, *args, **kwargs):
        print("Test Base Init")
        super().__init__(*args, **kwargs)
        self.driver = None
        self.platform = env('PLATFORM')
        self.platform_name = env('PLATFORM_NAME')
        self.platform_version = env('PLATFORM_VER')
        self.device_name = env('DEVICE_NAME')
        self.device_app_name=env('DEVICE_APP_NAME')
        self.device_app_package = env('DEVICE_APP_PACKAGE')
        self.device_app_activity = env('DEVICE_APP_ACTIVITY')
        self.device_browser_name = env('DEVICE_BROWSER_NAME')
        self.appium_server = env('APPIUM_SERVER')
        self.asus_router_url = env('ASUS_ROUTER_URL')
        self.asus_username= env('ASUS_USERNAME')
        self.asus_password = env('ASUS_PASSWORD')
        self.wait_timeout = env('WAIT_TIMEOUT')
        self.browser = env('BROWSER')
        self.headless = env('HEADLESS')
        self.test_log_file = env('TEST_LOG_FILE')
        self.current_platform = current_os
        self.root_dir = Path(__file__).resolve().parent.parent.parent
        self.drivers_dir = str(self.root_dir) + "\\drivers\\"
        print("drivers_dir", self.drivers_dir)

    def setUp(self) -> None:
        print("Test Base Setup")
        if self.platform == "WEB":
            self.browser_configurations()

        elif self.platform == "ANDROID":
            self.device_configurations()

        elif self.platform == "DESKTOP":
            print("Platform Desktop is initializing")

    def tearDown(self) -> None:
        print("Test Base Teardown")
        self.driver.quit()

    ############################################################################
    # Browser & Device setup
    # These methods are unique. It can be used by given configuration.
    ############################################################################
    def browser_configurations(self):
        browser_options = None
        if self.browser == "CHROME":
            browser_options = selenium_webdriver.ChromeOptions()
        elif self.browser == "FIREFOX":
            browser_options = selenium_webdriver.FirefoxOptions()
        elif self.browser == "EDGE":
            browser_options = selenium_webdriver.EdgeOptions()

        if self.headless:
            if current_os == "Windows":
                browser_options.add_argument('--headless')
            elif current_os == "Linux":
                browser_options.add_argument('--no-sandbox')
                browser_options.add_argument('--headless')
                browser_options.add_argument('--disable-dev-shm-usage')

        if current_os == "Linux":
            browser_options.add_argument("window-size=1920,1080")

        browser_options.add_argument('--ignore-ssl-errors=yes')
        browser_options.add_argument('--ignore-certificate-errors')
        browser_options.add_argument("--start-maximized")

        if self.browser == "CHROME":
            driver_path = self.drivers_dir+"chromedriver.exe"
            self.driver = selenium_webdriver.Chrome(executable_path=driver_path, options=browser_options)
        elif self.browser == "FIREFOX":
            driver_path = self.drivers_dir+"geckodriver.exe"
            self.driver = selenium_webdriver.Firefox(executable_path=driver_path, options=browser_options)
        elif self.browser == "EDGE":
            driver_path = self.drivers_dir+"msedgedriver.exe"
            self.driver = selenium_webdriver.Edge(executable_path=driver_path, options=browser_options)

    def device_configurations(self):
        desired_caps = {}
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformName'] = self.platform_name
        desired_caps['platformVersion'] = self.platform_version
        desired_caps['deviceName'] = self.platform_name
        desired_caps['udid'] = self.device_name
        desired_caps['autoGrantPermissions'] = True
        desired_caps['newCommandTimeout'] = 180  # 1 hour 15 minutes
        desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True

        if self.device_app_name == "Native":
            desired_caps['appPackage'] = self.device_app_package
            desired_caps['appActivity'] = self.device_app_activity

        elif self.device_app_name == "Hybrid":
            chromedriver_path = self.drivers_dir+"chromedriver.exe"
            desired_caps['browserName'] = self.device_browser_name
            desired_caps['chromedriverExecutable'] = chromedriver_path

        self.driver = appium_webdriver.Remote(self.appium_server, desired_caps)


    ############################################################################
    # Generic Methods
    # These methods are generic. It can be used by any module.
    ############################################################################
    def get(self, relative_url: str) -> None:
        self.driver.get(relative_url)

    def click(self, by: str, selector: str) -> Optional[WebElement]:
        element = self.find(by, selector)
        try:
            element.click()
        except Exception as ex:
            self.driver.execute_script("arguments[0].click();", element)

    def find(self, by: str, selector: str) -> Optional[WebElement]:
        element = self.driver.find_element(by, selector)
        self.assertTrue(element, 'Element cannot be found: "%s"' % selector)
        return element

    def click_element(self, by: str, element: str):
        self.driver.find_element(by, element).click()

    def type_text(self, by: str, element: str, value):
        self.driver.find_element(by, element).send_keys(value)

    def clear_and_type_text(self, by: str, element: str, value):
        self.driver.find_element(by, element).clear()
        self.waitForSeconds(1)
        self.driver.find_element(by, element).send_keys(value)

    def retrive_text(self, by: str, element: str):
        retrived_text = self.driver.find_element(by, element).text
        # print("Retrived Text -:- ", retrived_text)
        return retrived_text

    def verify_element_is_present(self, by: str, selector: str):
        element = self.driver.find_element(by, selector)
        element.is_displayed()

    def check_element_is_present(self, by: str, selector: str):
        status = False

        try:
            self.driver.find_element(by, selector)
            status = True
        except:
            status = False

        return status

    def move_to_element_by_text(self, text):
        element_visible = False
        max_scroll_count = 30
        scroll_count = 0
        while (not element_visible):
            try:
                self.driver.find_element_by_android_uiautomator(f"new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text(\"{text}\"));")
                self.waitForSeconds(1)
                #print("*** INFO: Element found...")
                element_visible = True
            except:
                self.waitForSeconds(1)
                scroll_count += 1
                if scroll_count == max_scroll_count:
                    self.assertTrue(False, f"*** ERROR: Element {text} is not visible after waiting for {scroll_count} time")
                    break

    def verify_element_not_present(self, by: str, selector: str):
        variables = None
        try:
            self.driver.find_element(by, selector)
            variables = True
        except NoSuchElementException:
            variables = False
        self.assertFalse(variables, f"*** INFO: Element {selector} expected to be not present but it is")

    def waitForSeconds(self, Seconds):
        time.sleep(Seconds)

    def wait_until_visible(self, by: str, element: str, timeout: int = 30):
        element_visible = False
        elapsed_time = 0
        while (not element_visible):
            try:
                elements = WebDriverWait(self.driver, 1).until(
                    EC.visibility_of_element_located((by, element)))
                element_visible = True
            except:
                self.waitForSeconds(1)
                elapsed_time += 1
                if elapsed_time == timeout:
                    self.assertTrue(False, f"*** ERROR: Element is not visible after waiting for {elapsed_time} seconds")
                    break

    def _alert_accept(self):
        try:
            self.waitForSeconds(1)
            WebDriverWait(self.driver, 30).until(EC.alert_is_present(), 'Timed out waiting for a popup to be appear.')
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert is Present -:- ")
        except:
            pass
            print("Alert is Not Present")

    def take_screen_shot(self, file_name, dir="screenshot_failures"):
        now = datetime.now()
        filename = file_name+"_"+now.strftime("%d%m%Y_%H%M%S")+".png"
        name = filename.replace(" ", "_")
        path = f"{dir}/{name}"
        self.driver.save_screenshot(path)
        return filename

    def log_test_result(self, page_title, test_id, log_message):
        current_time = datetime.utcnow()
        print(f'{current_time}, {page_title}, {test_id} {log_message}')
        content = ','.join(list([
            '{date:%Y-%m-%d %H:%M:%S}'.format(date=datetime.utcnow()),
            page_title,
            str(test_id),
            log_message,
        ]))
        with open(self.test_log_file, 'a') as f:
            f.write(content + '\n')

        if log_message.__eq__("FAIL"):
            name = page_title+"_"+test_id+".png"
            filename = name.replace(" ", "_")
            self.take_screen_shot(filename)

    ############################################################################
    # Generic Methods for Android device
    # These methods are generic. It can be used by any module.
    ############################################################################
    def launch_activity(self, packageName, activity):
        # Launching the Android File Manager
        self.driver.start_activity(packageName, activity)
        self.waitForSeconds(3)

    def close_activity(self, packageName):
        # Closing the Android File Manager
        self.driver.terminate_app(packageName)
        self.waitForSeconds(1)