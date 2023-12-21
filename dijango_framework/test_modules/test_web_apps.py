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
            self.driver.get(self.web_url)
            self.waitForSeconds(3)

            self.get(self.web_url)
            self.wait_until_visible(By.ID, "email")

            self.click(By.ID, "enterimg")
            self.waitForSeconds(2)
            self.wait_until_visible(By.XPATH, "//h1[contains(text(),'Automation Demo Site')]")
            self.click(By.XPATH, "//a[@href='Register.html']")
            self.waitForSeconds(2)
            self.wait_until_visible(By.XPATH, "//h2[contains(text(),'Register')]")
            self.type_text(By.XPATH, "//input[@placeholder='First Name']", "Demo First")
            self.type_text(By.XPATH, "//input[@placeholder='Last Name']", "Demo Second")
            self.type_text(By.XPATH, "//textarea[@ng-model='Adress']", "Demo Automation Site")
            self.type_text(By.XPATH, "//input[@ng-model='EmailAdress']", "demoSample@gmail.com")
            self.type_text(By.XPATH, "//input[@ng-model='Phone']", "2323456898")
            self.click(By.XPATH, "//input[@value='Male']")
            self.click(By.XPATH, "//input[@value='Cricket']")
            self.click(By.XPATH, "//input[@value='Movies']")
            self.click(By.XPATH, "//input[@value='Hockey']")
            self.scroll_down_web_page()
            self.waitForSeconds(3)
            self.select_dropdown_by_visible_text((By.ID, "Skills", "Android"),
                                                 (By.ID, "countries", "Select Country"),
                                                 (By.ID, "country", "India"))
            self.scroll_down_web_page()
            self.waitForSeconds(3)
            self.select_dropdown_by_visible_text((By.ID, "yearbox", "1991"),
                                                 (By.XPATH, "//select[@placeholder='Month']", "July"),
                                                 (By.ID, "daybox", "21"))
            self.scroll_down_web_page()
            self.waitForSeconds(3)
            self.type_text(By.ID, "firstpassword", self.password)
            self.type_text(By.ID, "secondpassword", self.password)
            self.click(By.ID, "submitbtn")
            self.waitForSeconds(3)

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")