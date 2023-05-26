import time
import pyperclip
from helpers.envhelper import EnvHandler
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MyAutoController:

    def __init__(self, driver):
        self.email = EnvHandler.get_env_var('LEVAN_USERNAME')
        self.password = EnvHandler.get_env_var('LEVAN_PAROL')
        self.driver = driver

    def register_car(self, car_drive_wheels, descr_text):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        self.choose_template()
        self.set_wheel()
        self.set_drive_wheels(car_drive_wheels)
        self.set_car_params()
        self.set_description(descr_text)
        self.configure_price()
        self.is_on_auction()
        self.publish()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def choose_template(self):
        scroll = self.driver.find_element(By.XPATH, '//div[contains(@class,"bg-white border-radius-m-14")]')
        scroll.click()
        template = self.driver.find_element(By.XPATH, "//div[text()='copart auto']")
        template.click()

    def set_wheel(self):
        wheel = self.driver.find_element(By.XPATH, "//div[text()='მარცხენა']")
        wheel.click()

    def set_drive_wheels(self, dr_wheel):
        if dr_wheel == '4x4':
            drive_wheels = self.driver.find_element(By.XPATH, "//div[text()='4x4']")
            drive_wheels.click()

    def set_car_params(self):
        spans = self.driver.find_elements(By.XPATH, '//span[contains(@class, "d-flex align-items-center justify-content-center w-16px h-16px mr-4px mr-md-8px")]')
        for span in spans:
            span.click()
        spans[len(spans)-1].click()

    def set_description(self, descr_text):
        textarea = self.driver.find_element(By.XPATH, '//textarea[contains(@class,"langs-textarea p-16px w-100 h-160px border-solid-1 border-gray-320 font-size-14 text-gray-800")]')
        copy_action = ActionChains(self.driver)
        pyperclip.copy(descr_text)
        textarea.click()
        copy_action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        textarea.send_keys(Keys.RETURN)

    def configure_price(self):
        price_input = self.driver.find_element(By.NAME, "sale.price")
        price_value = int(price_input.get_attribute("value"))
        if price_value < 1000:
            span = self.driver.find_element(By.XPATH, "//span[text()='ფასი შეთანხმებით']")
            span.click()

    def is_on_auction(self):
        span = self.driver.find_element(By.XPATH, "//span[text()='იყიდება აუქციონზე']")
        span.click()

    def publish(self):
        publish = self.driver.find_element(By.XPATH,
            '//button[contains(@class,"h-56px d-flex align-items-center justify-content-center border-radius-8 bg-orange px-24px px-md-36px border-0 text-white font-size-14 font-tbc-medium w-100 w-sm-50 w-sm-50 w-md-auto ")]')
        publish.click()

    def enter_myauto_account(self):
        self.driver.get('https://www.myauto.ge/ka')
        time.sleep(5)
        if self.driver.find_element(By.XPATH, '//div[contains(@class, "d-none")]').text == 'ავტორიზაცია':
            self.authorization()
            self.handle_warning_modal()
            self.handle_email()
            self.handle_password()
            time.sleep(5)
        else:
            return

    def authorization(self):
        auth = self.driver.find_element(By.XPATH, '//div[contains(@class, "d-none")]')
        auth.click()

    def handle_email(self):
        email = self.driver.find_element(By.ID, 'Email')
        email.send_keys(self.email)

    def handle_password(self):
        password = self.driver.find_element(By.ID, "Password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

    def handle_warning_modal(self):
        wait = WebDriverWait(self.driver, 10)
        warning_modal = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="Modal1"]')))
        if warning_modal:
            modal_btn = warning_modal.find_element(By.XPATH, './/button[contains(@class,"gradient-button")]')
            modal_btn.click()
        else:
            return


