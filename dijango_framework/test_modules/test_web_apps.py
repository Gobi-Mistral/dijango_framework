import traceback

from selenium.webdriver.common.by import By

from dijango_framework.helper.test_base import TestBase

module_name = "WEB BROWSER"

class TestBrowser(TestBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def test_001_open_browser(self):
        test_case_id = "WEB_BROWSER_TC_001"

        try:
            self.driver.get(self.asus_router_url)
            self.waitForSeconds(3)

            self.get(self.asus_router_url)
            self.wait_until_visible(By.XPATH, "//div[@onclick='login();']")

            self.type_text(By.XPATH, "//input[@id='login_username']", self.asus_username)
            self.type_text(By.XPATH, "//input[@name='login_passwd']", self.asus_username)
            self.clear_and_type_text(By.XPATH, "//input[@name='login_passwd']", self.asus_password)
            self.click(By.XPATH, "//div[@onclick='login();']")
            self.wait_until_visible(By.XPATH, "//span[text()='RT-AX3000']")

            self.waitForSeconds(2)
            # Logout
            text = self.retrive_text(By.XPATH, "//span[text()='Logout']")
            print("Retrived Text ", text)
            self.wait_until_visible(By.XPATH, "//span[text()='Logout']")
            self.click(By.XPATH, "//span[text()='Logout']")
            self._alert_accept()
            self.waitForSeconds(1)

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")