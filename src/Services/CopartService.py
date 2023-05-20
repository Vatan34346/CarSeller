import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CopartService:
    def __init__(self):
        self.driver = wb.Chrome(service=Service(ChromeDriverManager().install()))

    def go_to_car_inventory(self):
        self.driver.get('https://www.copart.com/vehicleFinderSearch?searchStr=%7B%22MISC%22:%5B%22%23VehicleTypeCode:VEHTYPE_V%22,%22%23OdometerReading:%5B0%20TO%209999999%5D%22,%22%23LotYear:%5B2013%20TO%202024%5D%22%5D,%22sortByZip%22:false,%22buyerEnteredZip%22:null,%22milesAway%22:null%7D%20&displayStr=%5B0%20TO%209999999%5D,%5B2013%20TO%202024%5D&from=%2FvehicleFinder')
        time.sleep(10)