import traceback

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dijango_framework.helper.test_base import TestBase

module_name = "WEB BROWSER"

class TestDesktop(TestBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def test_001_calculator_app(self):
        test_case_id = "DESKTOP_APP_TC_001"

        try:
            self.waitForSeconds(5)
            # Find and interact with Calculator elements
            self.click_form((By.NAME, "One"),
                            (By.NAME, "Plus"),
                            (By.NAME, "Two"),
                            (By.NAME, "Equals"))

            # Retrieve and print the result
            result = self.retrive_text(By.ACCESSIBILITY_ID, "CalculatorResults")
            print(f"Calculator Result: {result}")

            self.click_form((By.NAME, "Seven"),
                            (By.NAME, "Multiply by"),
                            (By.NAME, "Nine"),
                            (By.NAME, "Plus"),
                            (By.NAME, "One"),
                            (By.NAME, "Equals"),
                            (By.NAME, "Divide by"),
                            (By.NAME, "Eight"),
                            (By.NAME, "Equals"))

            # Retrieve and print the result
            result = self.retrive_text(By.ACCESSIBILITY_ID, "CalculatorResults")
            print(f"Calculator Result: {result}")

            self.click_form((By.NAME, "Eight"),
                            (By.NAME, "Eight"),
                            (By.NAME, "Divide by"),
                            (By.NAME, "One"),
                            (By.NAME, "One"),
                            (By.NAME, "Equals"))

            # Retrieve and print the result
            result = self.retrive_text(By.ACCESSIBILITY_ID, "CalculatorResults")
            print(f"Calculator Result: {result}")

            self.click_form((By.NAME, "Nine"),
                            (By.NAME, "Multiply by"),
                            (By.NAME, "Nine"),
                            (By.NAME, "Equals"))

            # Retrieve and print the result
            result = self.retrive_text(By.ACCESSIBILITY_ID, "CalculatorResults")
            print(f"Calculator Result: {result}")

            self.click_form((By.NAME, "Nine"),
                            (By.NAME, "Minus"),
                            (By.NAME, "One"),
                            (By.NAME, "Equals"))

            # Retrieve and print the result
            result = self.retrive_text(By.ACCESSIBILITY_ID, "CalculatorResults")
            print(f"Calculator Result: {result}")

            self.waitForSeconds(5)

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    def test_002_activation_key_generator(self):
        test_case_id = "DESKTOP_APP_TC_002"

        try:
            self.waitForSeconds(2)

            result = self.retrive_text(By.ACCESSIBILITY_ID, "1003")
            print(f"Lable Name : {result}")
            result = self.retrive_text(By.ACCESSIBILITY_ID, "1018")
            print(f"App Version : {result}")

            self.click(By.ACCESSIBILITY_ID, "1001")

            lable = self.retrive_text(By.ACCESSIBILITY_ID, "1007")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "1025")
            print(f"Settings {lable} : {value}")
            lable = self.retrive_text(By.ACCESSIBILITY_ID, "1026")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "1027")
            print(f"Settings {lable} : {value}")
            lable = self.retrive_text(By.ACCESSIBILITY_ID, "1029")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "1028")
            print(f"Settings {lable} : {value}")
            self.click(By.ACCESSIBILITY_ID,  "2")

            self.click(By.ACCESSIBILITY_ID, "1011")
            # self.desktop_verify_element_present("XPATH", "//*[@AutomationId='TitleBar']")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "65535")
            print(f"Generate Popup : {value}")
            self.click(By.NAME, "OK")

            self.click(By.ACCESSIBILITY_ID,  "1010")
            # self.desktop_verify_element_present("XPATH", "//*[@AutomationId='TitleBar']")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "65535")
            print(f"Submit Popup : {value}")
            self.click(By.NAME, "OK")

            self.type_text(By.ACCESSIBILITY_ID, "1017", "123456789231")
            self.type_text(By.ACCESSIBILITY_ID, "1016", "Dr.Jhon David")
            self.type_text(By.ACCESSIBILITY_ID, "1013", "Texas Pharmacy")
            self.type_text(By.ACCESSIBILITY_ID, "1023", "Washington")
            self.type_text(By.ACCESSIBILITY_ID, "1027", "United States")
            self.type_text(By.ACCESSIBILITY_ID, "1029", "Texas")
            self.type_text(By.ACCESSIBILITY_ID, "1031", "U.S.A")
            self.type_text(By.ACCESSIBILITY_ID, "1034", "1008456")
            self.type_text(By.ACCESSIBILITY_ID, "1014", "sampledemo.com")
            self.type_text(By.ACCESSIBILITY_ID, "1015", "1234567809")

            self.click(By.ACCESSIBILITY_ID,  "1011")
            self.waitForSeconds(3)
            lable = self.retrive_text(By.ACCESSIBILITY_ID, "1009")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "1012")
            print(f"Generated Key {lable} : {value}")

            self.click(By.ACCESSIBILITY_ID, "1010")
            self.wait_until_visible(By.ACCESSIBILITY_ID, "65535")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "65535")
            print(f"Submit Popup {lable} : {value}")
            self.click(By.NAME, "OK")

            self.click(By.ACCESSIBILITY_ID,  "1001")

            self.type_text(By.ACCESSIBILITY_ID, "1025", "scripability.licensing@gmail.com")
            xpath = "//*[@AutomationId='1027' and @Name='Password:']"
            self.type_text(By.XPATH, xpath, "uRo8n^sT7hBe")
            self.clear_and_type_text(By.ACCESSIBILITY_ID, "1028", "587")
            self.click(By.ACCESSIBILITY_ID,  "1")

            self.click(By.ACCESSIBILITY_ID,  "1010")
            self.wait_until_visible(By.ACCESSIBILITY_ID, "65535")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "65535")
            print(f"Submit Popup {lable} : {value}")
            self.click(By.NAME, "OK")

            self.clear_and_type_text(By.ACCESSIBILITY_ID, "1014", "sampleDemo@gmail.com")
            self.click(By.ACCESSIBILITY_ID,  "1010")
            self.wait_until_visible(By.ACCESSIBILITY_ID, "65535")
            value = self.retrive_text(By.ACCESSIBILITY_ID, "65535")
            print(f"Submit Popup {lable} : {value}")
            self.click(By.NAME, "OK")

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    def test_003_interface_test_server(self):
        test_case_id = "DESKTOP_APP_TC_003"

        try:
            self.waitForSeconds(2)
            result = self.retrive_text(By.XPATH, "//*[@AutomationId='1011']")
            print(f"App Version : {result}")

            self.driver.find_element(By.ACCESSIBILITY_ID, "1005").click()
            print("Accessibility_ID Done")

            # self.click(By.XPATH, "//*[@AutomationId='1005' and @Name='Start']")
            value = self.retrive_text(By.XPATH, "//*[@AutomationId='65535']")
            print(f"Query Port Popup : {value}")
            self.click_element(By.XPATH, "//*[@Name='OK']")
            self.type_text(By.XPATH, "//*[@AutomationId='1003']", "1900")
            self.click(By.XPATH, "//*[@AutomationId='1005' and @Name='Start']")
            value = self.retrive_text(By.XPATH, "//*[@AutomationId='65535']")
            print(f"Query Responce Data Popup : {value}")
            self.click_element(By.XPATH, "//*[@Name='OK']")

            self.select_pharmacy("BestRx")

            self.fill_form((By.XPATH, "//*[@AutomationId='1007']", "RX123NDC43500"),
                            (By.XPATH, "//*[@AutomationId='1023']", "120"),
                            (By.XPATH, "//*[@AutomationId='1025']", "112"),
                            (By.XPATH, "//*[@AutomationId='1013']", "Jhon David"),
                            (By.XPATH, "//*[@AutomationId='1027']", "Next appointment on december 1st week"),
                            (By.XPATH, "//*[@AutomationId='1019']", "Dollo Tera 250 MG"),
                            (By.XPATH, "//*[@AutomationId='1021']", "Take 1 medicine on each for after food and don't drink hot water"),
                            (By.XPATH, "//*[@AutomationId='1033']", "23456798342"),
                            (By.XPATH, "//*[@AutomationId='1029']", "Dr.Miller"),
                            (By.XPATH, "//*[@AutomationId='1031']", "Texas Pharmacy"),
                            (By.XPATH, "//*[@AutomationId='1039']", "December 05 2023"),
                            (By.XPATH, "//*[@AutomationId='1036']", "October 12 2023"),
                            (By.XPATH, "//*[@AutomationId='1037']", "December 01 2023"),
                            (By.XPATH, "//*[@AutomationId='1053']", "If you have any concern about this medicine, please contact pharmacy"))

            self.click(By.XPATH, "//*[@AutomationId='1046']")

            self.fill_form((By.ACCESSIBILITY_ID, "1041", "Keep in refrigerator. Do not freeze."),
                           (By.ACCESSIBILITY_ID, "1043", "Bring to room temperature before preparing for use."),
                           (By.ACCESSIBILITY_ID, "1042", "If brought to room temperature, this product expires after."),
                           (By.ACCESSIBILITY_ID, "1044", "Do not shake."),
                           (By.ACCESSIBILITY_ID, "1045", "Protect from light."))

            self.click_element(By.XPATH, "//*[@Name='Submit']")
            value = self.retrive_text(By.XPATH, "//*[@AutomationId='1004']")
            print(f"Responced Query : {value}")
            self.click_element(By.XPATH, "//*[@Name='Start']")

            self.verify_element_is_present(By.XPATH, "//*[@Name='Stop']")
            self.click_element(By.XPATH, "//*[@Name='Stop']")
            value = self.retrive_text(By.XPATH, "//*[@AutomationId='65535']")
            print(f"Query Stop Popup : {value}")
            self.click_element(By.XPATH, "//*[@Name='OK']")
            self.verify_element_is_present(By.XPATH, "//*[@Name='Start']")

            self.click_element(By.NAME, "Query Data")
            self.waitForSeconds(2)
            result = self.retrive_text(By.XPATH, "//*[@AutomationId='1014']")
            print(f"Query Data App Version : {result}")
            self.driver.find_element(By.NAME, "Fetch Query").click()
            value = self.retrive_text(By.XPATH, "//*[@AutomationId='65535']")
            print(f"Query Port Popup : {value}")
            self.click_element(By.XPATH, "//*[@Name='OK']")
            self.select_pharmacy_query_data("Liberty Software")
            self.type_text(By.ACCESSIBILITY_ID, "1007", "RX124034567")
            self.click(By.NAME, "Fetch Query")
            self.waitForSeconds(2)
            result = self.retrive_text(By.XPATH, "//*[@AutomationId='1012']")
            print(f"Fetched Query Data Response : {result}")

            self.click_element(By.NAME, "Response Data")
            self.waitForSeconds(2)
            self.select_pharmacy("None")

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    def test_004_desktop_groove_music_app(self):
        test_case_id = "DESKTOP_APP_TC_004"

        try:
            self.wait_until_visible(By.ACCESSIBILITY_ID, "NavMenuButton")
            self.driver.find_element(By.ACCESSIBILITY_ID, "NavMenuButton").click()
            self.waitForSeconds(2)

            self.wait_until_visible(By.NAME, "Playlists")
            self.driver.find_element(By.NAME, "Playlists").click()
            self.waitForSeconds(2)

            self.wait_until_visible(By.ACCESSIBILITY_ID, "PlaylistsPage")
            txt = self.retrive_text(By.ACCESSIBILITY_ID, "FilteredEmptyPageTitle")
            print("PlayList Page Details -:- ", txt)
            self.waitForSeconds(2)

            self.click_element(By.ACCESSIBILITY_ID, "Command_CreatePlaylistCommand")
            self.waitForSeconds(2)

            self.wait_until_visible(By.ACCESSIBILITY_ID, "CreatePlaylist")
            name = "MY_PLAY_LIST"
            self.type_text(By.ACCESSIBILITY_ID, "PlaylistName", name)
            txt = self.retrive_text(By.ACCESSIBILITY_ID, "Attribution")
            print("Who is Created -:- ", txt)
            self.click_element(By.ACCESSIBILITY_ID, "CreatePlaylist")
            self.waitForSeconds(2)
            self.wait_until_visible(By.XPATH, f"//*[contains(@Name,'Basic info for')]")
            self.verify_element_is_present(By.XPATH, f"//*[contains(@Name,'Basic info for {name}')]")

            self.click_element(By.ACCESSIBILITY_ID, "NavigateBackButton")
            self.waitForSeconds(2)

            self.click_element(By.XPATH, f"//*[contains(@Name,'{name}')]")
            self.wait_until_visible(By.XPATH, f"//*[contains(@Name,'Basic info for')]")
            txt = self.retrive_text(By.XPATH, f"//*[contains(@Name,'Basic info for')]")
            print("Created PlayList Page Name -:- ", txt)
            self.verify_element_is_present(By.XPATH, f"//*[contains(@Name,'Basic info for {name}')]")

            self.waitForSeconds(6)

            self.click_element(By.NAME, "Add songs from my collection, Go to Albums")
            self.wait_until_visible(By.XPATH, f"//*[@Name='Songs']")
            self.click_element(By.XPATH, f"//*[@Name='Songs']")
            self.waitForSeconds(2)

            # self.click_element(By.XPATH, "//*[@Name='Not finding everything?, Show us where to look for music,']")
            # self.waitForSeconds(2)
            # self.wait_until_visible(By.NAME, "Build your collection from your local music files")
            # txt = self.retrive_text(By.NAME, "Build your collection from your local music files")
            # print("Add songs into the Playlist Popup -:- ", txt)
            # self.click_element(By.XPATH, f"//*[@Name='Add folder']")
            # self.waitForSeconds(2)
            #
            # self.click_element(By.XPATH, f"//*[@Name='Music']")
            # self.waitForSeconds(2)
            # self.click_element(By.XPATH, f"//*[@Name='Add this folder to Music']")
            # self.waitForSeconds(2)
            # self.click_element(By.XPATH, f"//*[@Name='Done']")
            # self.waitForSeconds(2)

            self.click_element(By.XPATH, f"//*[@Name='mp3_8000']")
            self.waitForSeconds(2)
            self.click_element(By.XPATH, f"//*[@Name='Play all']")
            self.waitForSeconds(6)
            self.click_element(By.XPATH, f"//*[@Name='Pause']")
            self.waitForSeconds(2)

            self.wait_until_visible(By.ACCESSIBILITY_ID, "NavMenuButton")
            self.driver.find_element(By.ACCESSIBILITY_ID, "NavMenuButton").click()
            self.waitForSeconds(2)
            self.wait_until_visible(By.NAME, "Playlists")
            self.driver.find_element(By.NAME, "Playlists").click()
            self.waitForSeconds(2)

            self.click_element(By.XPATH, f"//*[contains(@Name,'{name}')]")
            self.wait_until_visible(By.XPATH, f"//*[contains(@Name,'Basic info for')]")

            self.click_element(By.ACCESSIBILITY_ID, "Command_MoreCommand")
            self.waitForSeconds(1)
            self.click_element(By.NAME, "Delete")

            self.wait_until_visible(By.ACCESSIBILITY_ID, "MessageTextBox")
            txt = self.retrive_text(By.ACCESSIBILITY_ID, "MessageTextBox")
            print("PlayList Page Delete Details -:- ", txt)
            self.waitForSeconds(2)

            self.click_element(By.NAME, "OK")
            self.waitForSeconds(2)

            self.wait_until_visible(By.ACCESSIBILITY_ID, "PlaylistsPage")
            txt = self.retrive_text(By.ACCESSIBILITY_ID, "FilteredEmptyPageTitle")
            self.verify_element_is_present(By.NAME, "Nothing to show here. Try a different filter.")
            print("PlayList Page Details -:- ", txt)
            self.waitForSeconds(2)

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    def test_005_desktop_app(self):
        test_case_id = "DESKTOP_APP_TC_005"

        try:
            self.wait_until_visible(By.ACCESSIBILITY_ID, "NavMenuButton")


        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    ############################################################################
    # Generic Methods for Desktop specific apps
    ############################################################################
    def select_pharmacy(self, pharmacy_name):
        self.click(By.XPATH, "//*[@AutomationId='1016']")
        self.click_element(By.XPATH, f"//*[@Name='{pharmacy_name}']")
        self.waitForSeconds(3)

    def select_pharmacy_query_data(self, pharmacy_name):
        self.click(By.XPATH, "//*[@AutomationId='1006']")
        self.click_element(By.XPATH, f"//*[@Name='{pharmacy_name}']")
        self.waitForSeconds(3)
