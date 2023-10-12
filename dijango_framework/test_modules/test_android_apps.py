import traceback

from selenium.webdriver.common.by import By

from dijango_framework.helper.test_base import TestBase

module_name = "Android Device"
class TestAndroidDevice(TestBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_001_open_settings(self):
        test_case_id = "ANDROID_DEVICE_TC_001"
        bt_device = ""

        try:
            self.launch_activity("com.android.settings", "com.android.settings.Settings")

            self.move_to_element_by_text("Connected devices")
            self.wait_until_visible(By.XPATH, "//*[@resource-id='android:id/title' and @text='Connected devices']")
            self.click_element(By.XPATH, "//*[@resource-id='android:id/title' and @text='Connected devices']")
            self.wait_until_visible(By.XPATH, "//*[@resource-id='android:id/title' and @text='Other devices']")

            self.waitForSeconds(2)

            try:
                self.move_to_element_by_text("See all")
                self.wait_until_visible(By.XPATH, "//*[@resource-id='android:id/title' and @text='See all']")
                self.click_element(By.XPATH, "//*[@resource-id='android:id/title' and @text='See all']")
                self.waitForSeconds(3)
                self.verify_element_is_present(By.XPATH, f"//*[@resource-id='android:id/title' and @text='{bt_device}']")

                self.verify_element_is_present(By.XPATH, f"//*[@resource-id='android:id/title' and @text='{bt_device}']/parent::android.widget.RelativeLayout//following-sibling::android.widget.LinearLayout//android.widget.ImageView[@content-desc='Settings']")
                self.click_element(By.XPATH, f"//*[@resource-id='android:id/title' and @text='{bt_device}']/parent::android.widget.RelativeLayout//following-sibling::android.widget.LinearLayout//android.widget.ImageView[@content-desc='Settings']")

                self.wait_until_visible(By.XPATH, f"//*[@resource-id='com.android.settings:id/entity_header_title' and @text='{bt_device}']")
                self.verify_element_is_present(By.XPATH, f"//*[@resource-id='com.android.settings:id/entity_header_title' and @text='{bt_device}']")

                self.wait_until_visible(By.XPATH, f"//*[@resource-id='com.android.settings:id/entity_header_title' and @text='{bt_device}']")
                self.click_element(By.XPATH, "//*[@resource-id='com.android.settings:id/button1' and @text='FORGET']")
                self.wait_until_visible(By.XPATH, f"//*[@resource-id='com.android.settings:id/alertTitle' and @text='Forget device?']")
                self.verify_element_is_present(By.XPATH, f"//*[@resource-id='android:id/message' and @text='Your phone will no longer be paired with {bt_device}']")
                self.verify_element_is_present(By.XPATH, "//*[@resource-id='android:id/button1' and @text='FORGET DEVICE']")
                self.click_element(By.XPATH, "//*[@resource-id='android:id/button1' and @text='FORGET DEVICE']")
            except Exception as ex:
                print("There is no previously connected devices")

            self.close_activity("com.android.settings")

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False,  f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")