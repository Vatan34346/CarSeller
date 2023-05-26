import time
import pyautogui
from helpers.desriptionHelper import MyAutoTemplateDescriptionHandler
from Services.myautoService import MyAutoController
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as wb
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException


class CopartService:
    def __init__(self):
        self.options = Options()
        self.options.add_extension('CRXs/extension_5_0_0_0.crx')
        self.driver = wb.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.maximize_window()
        self.chains = ActionChains(self.driver)
        self.my_auto = MyAutoController(self.driver)

    def process_cars_to_mauto(self):
        self.my_auto.enter_myauto_account()
        self.go_to_car_inventory()
        self.manage_cars_data(self.get_cars_from_page())
        for p_numb in range(1, 100):
            self.get_next_page(p_numb)
            while True:
                try:
                    self.manage_cars_data(self.get_cars_from_page())
                    break
                except NoSuchElementException:
                    print('No Such element')
                except NoSuchWindowException:
                    print('No Such Window Exception')
                except StaleElementReferenceException:
                    print('Stale Element error')

    def get_next_page(self, page_value):
        time.sleep(10)
        page_button = self.driver.find_element(By.XPATH, f"//button[text()={str(page_value)}]")
        page_button.click()

    def manage_cars_data(self, car_hrefs):
        for href in car_hrefs:
            self.driver.get(href)
            time.sleep(10)
            descr = self.description()
            car_drive = self.get_car_drive(self.driver.find_element(By.XPATH, "//span[@data-uname='DriverValue']").text)
            pyautogui.rightClick()
            time.sleep(5)
            self.my_auto.register_car(car_drive, descr)
            self.driver.back()

    def get_cars_from_page(self):
        links = self.driver.find_elements(By.XPATH, '//a[contains(@class, "ng-star-inserted")]')
        href = []
        for item in links:
            if isinstance(item.get_attribute('href'), str):
                if 'lot' in item.get_attribute('href'):
                    href.append(item.get_attribute('href'))
        return list(set(href))

    def go_to_car_inventory(self):
        self.driver.get('https://www.copart.com/vehicleFinderSearch?displayStr=%5B0%20TO%209999999%5D,%5B2013%20TO%202024%5D&from=%2FnoSearchResults%3FdisplayStr%3D%5B145300%20TO%209999999%5D,%5B2013%20TO%202024%5D,Lexus,Lx470&query=&searchCriteria=%7B%22query%22:%5B%22*%22%5D,%22filter%22:%7B%22VEHT%22:%5B%22vehicle_type_code:VEHTYPE_V%22%5D,%22FETI%22:%5B%22lot_condition_code:CERT-D%22%5D,%22TITL%22:%5B%22title_group_code:TITLEGROUP_C%22%5D,%22BODY%22:%5B%22body_style:%5C%222DR%20SPOR%5C%22%22,%22body_style:%5C%224DR%20SPOR%5C%22%22,%22body_style:%5C%224DR%20EXT%5C%22%22,%22body_style:%5C%22COUPE%5C%22%22,%22body_style:%5C%22COUPE%203D%5C%22%22,%22body_style:%5C%22CONVERTI%5C%22%22,%22body_style:%5C%22HATCHBAC%5C%22%22,%22body_style:%5C%22SEDAN%204D%5C%22%22,%22body_style:%5C%22SPORTS%20V%5C%22%22,%22body_style:%5C%22PICKUP%5C%22%22,%22body_style:%5C%22CARGO%20VA%5C%22%22%5D,%22ODM%22:%5B%22%23OdometerReading:%5B0%20TO%209999999%5D%22%5D,%22YEAR%22:%5B%22%23LotYear:%5B2013%20TO%202024%5D%22%5D%7D,%22searchName%22:%22%22,%22watchListOnly%22:false,%22freeFormSearch%22:false%7D')
        time.sleep(5)

    def description(self):
        car_lot = self.driver.find_element(By.XPATH, '//span[contains(@class,"one-click-select")]')
        mauto_descr_helper = MyAutoTemplateDescriptionHandler(car_lot.text)
        descr = mauto_descr_helper.get_description()
        return descr

    def get_car_drive(self, car_drive_text):
        if car_drive_text.startswith('4x4'):
            return '4x4'
        else:
            return car_drive_text













