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

    def test_001_place_online_order(self):
        test_case_id = "WEB_BROWSER_TC_001"

        try:
            self.driver.get(self.web_url)
            self.waitForSeconds(3)

            self.wait_until_visible(By.XPATH, "//div[@class='login_logo' and contains(text(),'Swag Labs')]")
            self.verify_element_is_present(By.ID, "user-name")
            self.verify_element_is_present(By.ID, "password")
            self.verify_element_is_present(By.ID, "login-button")
            self.verify_element_is_present(By.ID, "login_credentials")
            self.verify_element_is_present(By.XPATH, "//div[@class='login_password']")
            username = self.retrive_text(By.ID, "login_credentials")
            password = self.retrive_text(By.XPATH, "//div[@class='login_password']")
            print("Username's -:- ", username)
            print("Password -:- ", password)
            self.click(By.ID, "login-button")
            self.wait_until_visible(By.XPATH, "//h3[@data-test='error']")
            login_error = self.retrive_text(By.XPATH, "//h3[@data-test='error']")
            print("Login Error Message -:- ", login_error)
            self.assertEqual(login_error, "Epic sadface: Username is required", f"*** ERROR: Login error msg is not matched the expected msg {login_error}")
            self.click(By.XPATH, "//button[@class='error-button']")

            user_name = username.replace("Accepted usernames are:", "").split()
            print("User Names -:- ", user_name)
            pass_word = password.replace("Password for all users:", "").split()
            print("Pass Word -:- ", pass_word)
            self.type_text(By.ID, "user-name", user_name[0])
            self.type_text(By.ID, "password", pass_word[0])
            self.click(By.ID, "login-button")
            self.waitForSeconds(3)
            self.wait_until_visible(By.ID, "react-burger-menu-btn")
            self.verify_element_is_present(By.ID, "shopping_cart_container")

            product_name = "Sauce Labs Backpack"
            product_link = f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']"
            self.verify_element_is_present(By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']")
            product_title = self.retrive_text(By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']")
            product_description = self.retrive_text(By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']/parent::a/following-sibling::div[@class='inventory_item_desc']")
            product_price = self.retrive_text(By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']/parent::a/parent::div/following-sibling::div[@class='pricebar']/div[@class='inventory_item_price']")
            add_cart_button = f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']/parent::a/parent::div/following-sibling::div[@class='pricebar']/button[text()='Add to cart']"
            cart_remove_button = f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']/parent::a/parent::div/following-sibling::div[@class='pricebar']/button[text()='Remove']"

            self.verify_element_is_present(By.XPATH, add_cart_button)
            self.click(By.XPATH, add_cart_button)
            self.waitForSeconds(2)
            self.verify_element_is_present(By.XPATH, cart_remove_button)
            self.click(By.XPATH, product_link)
            self.wait_until_visible(By.ID, "back-to-products")
            self.waitForSeconds(3)

            self.wait_until_visible(By.XPATH, "//div[contains(@class,'inventory_details_name')]")
            product_details_title = self.retrive_text(By.XPATH, "//div[contains(@class,'inventory_details_name')]")
            product_details_description = self.retrive_text(By.XPATH, "//div[contains(@class,'inventory_details_name')]/following-sibling::div[contains(@class,'inventory_details_desc')]")
            product_details_price = self.retrive_text(By.XPATH, "//div[contains(@class,'inventory_details_name')]//following-sibling::div[contains(@class,'inventory_details_price')]")
            remove_button = "//div[contains(@class,'inventory_details_name')]//following-sibling::button[contains(@id,'remove')]"
            self.verify_element_is_present(By.XPATH, remove_button)

            self.assertEqual(product_title, product_details_title, f"*** ERROR: Expected title is not matched with actual, Exp is {product_title} Act is {product_details_title}")
            self.assertEqual(product_description, product_details_description, f"*** ERROR: Expected description is not matched with actual, Exp is {product_description} Act is {product_details_description}")
            self.assertEqual(product_price, product_details_price, f"*** ERROR: Expected price is not matched with actual, Exp is {product_price} Act is {product_details_price}")

            self.click(By.ID, "back-to-products")
            self.wait_until_visible(By.XPATH, f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']")
            self.waitForSeconds(3)

            self.click(By.ID, "shopping_cart_container")
            self.wait_until_visible(By.XPATH, "//span[@class='title' and text()='Your Cart']")
            cart_product_title = self.retrive_text(By.XPATH, "//div[@class='inventory_item_name']")
            cart_product_description = self.retrive_text(By.XPATH, "//div[@class='inventory_item_desc']")
            cart_product_price = self.retrive_text(By.XPATH, "//div[@class='inventory_item_price']")
            self.waitForSeconds(3)

            self.assertEqual(product_title, cart_product_title, f"*** ERROR: Expected title is not matched with actual, Exp is {product_title} Act is {product_details_title}")
            self.assertEqual(product_description, cart_product_description, f"*** ERROR: Expected description is not matched with actual, Exp is {product_description} Act is {product_details_description}")
            self.assertEqual(product_price, cart_product_price, f"*** ERROR: Expected price is not matched with actual, Exp is {product_price} Act is {product_details_price}")

            self.click(By.ID, "checkout")
            self.wait_until_visible(By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']")
            self.verify_element_is_present(By.ID, "continue")
            self.verify_element_is_present(By.ID, "cancel")
            self.waitForSeconds(3)

            self.click(By.ID, "continue")
            self.waitForSeconds(2)
            error = self.retrive_text(By.XPATH, "//h3[@data-test='error']")
            self.assertEqual(error, "Error: First Name is required", f"*** ERROR: First Name error msg is mismatched Exp is 'Error: First Name is required' but Act is {error}")
            print("Check User Name Error Info -:- ", error)

            self.click(By.XPATH, "//h3[@data-test='error']/button[@class='error-button']")
            self.type_text(By.ID, "first-name", "Demo First")
            self.click(By.ID, "continue")
            self.waitForSeconds(2)
            error = self.retrive_text(By.XPATH, "//h3[@data-test='error']")
            self.assertEqual(error, "Error: Last Name is required", f"*** ERROR: Last Name error msg is mismatched Exp is 'Error: Last Name is required' but Act is {error}")
            print("Check User Name Error Info -:- ", error)

            self.click(By.XPATH, "//h3[@data-test='error']/button[@class='error-button']")
            self.type_text(By.ID, "last-name", "Demo Last")
            self.click(By.ID, "continue")
            self.waitForSeconds(2)
            error = self.retrive_text(By.XPATH, "//h3[@data-test='error']")
            self.assertEqual(error, "Error: Postal Code is required", f"*** ERROR: Postal Code error msg is mismatched Exp is 'Error: Postal Code is required' but Act is {error}")
            print("Check User Name Error Info -:- ", error)

            self.click(By.XPATH, "//h3[@data-test='error']/button[@class='error-button']")
            self.type_text(By.ID, "postal-code", "600100")
            self.click(By.ID, "continue")
            self.waitForSeconds(3)

            self.wait_until_visible(By.XPATH, "//div[@class='summary_info']//div[@class='summary_value_label']")
            self.verify_element_is_present(By.ID, "finish")
            self.verify_element_is_present(By.ID, "cancel")
            payment_information = self.retrive_text(By.XPATH, "//div[@class='summary_info']//div[@class='summary_value_label'][1]")
            shipping_information = self.retrive_text(By.XPATH, "//div[@class='summary_info']//div[@class='summary_value_label'][2]")
            price_total = self.retrive_text(By.XPATH, "//div[@class='summary_info']//div[@class='summary_subtotal_label']")
            price_tax = self.retrive_text(By.XPATH, "//div[@class='summary_info']//div[@class='summary_tax_label']")
            total_price = self.retrive_text(By.XPATH, "//div[@class='summary_info']//div[@class='summary_info_label summary_total_label']")
            print("Payment Information -:- ", payment_information)
            print("Shipping Information -:- ", shipping_information)
            print("Product Price Total -:- ", price_total)
            print("Tax Price -:- ", price_tax)
            print("Total Price -:- ", total_price)
            self.waitForSeconds(3)

            self.click(By.ID, "finish")
            self.waitForSeconds(3)
            self.verify_element_is_present(By.XPATH, "//h2[@class='complete-header']")
            confirm_message = self.retrive_text(By.XPATH, "//h2[@class='complete-header']")
            delivery_info = self.retrive_text(By.XPATH, "//div[@class='complete-text']")
            self.assertEqual(confirm_message, "Thank you for your order!", f"*** ERROR: Expected confirm msg is 'Thank you for your order!' but Actual is {confirm_message}")
            print("Product Placement Confirm Message -:- ", confirm_message)
            print("Product Delivery Information -:- ", delivery_info)

            self.click(By.ID, "back-to-products")
            self.waitForSeconds(3)

            self.click(By.ID, "react-burger-menu-btn")
            self.waitForSeconds(2)
            self.click(By.ID, "logout_sidebar_link")
            self.waitForSeconds(5)

        except Exception as ex:
            print(f"Exception occurred: {ex}")
            self.log_test_result(f'{module_name}', f'{test_case_id}', "FAIL")
            self.assertTrue(False, f"*** ERROR: Test case {test_case_id} failed due to exception {ex} {traceback.format_exc()}")

    def x_test_001_open_browser(self):
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
