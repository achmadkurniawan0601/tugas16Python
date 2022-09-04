import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestTime(unittest.TestCase):  # TEST SCENARIO LOGIN

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # 1. view all employee name
    def test_case07(self):
        # Login
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        # Click Menu Time
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        #validasi
        userName = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/h6").text
        self.assertIn("",userName)
        time.sleep(3)

    # 2. view employee name person
    def test_case08(self):
        # Login
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        # Click Menu Time
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        # Input Employee Name
        # browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input").send_keys("Paul Collings")
        # time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button").click()
        time.sleep(1)

        #validasi
        userName = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/h6").text
        self.assertIn('Timesheet for', userName)
        # time.sleep(3)

    def tearDown(self): 
        self.browser.close()
 
if __name__ == "__main__": 
    unittest.main()