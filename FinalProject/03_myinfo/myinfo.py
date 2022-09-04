import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestInfo(unittest.TestCase):  # TEST SCENARIO LOGIN

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # 1. view profile info
    def test_case09(self):
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

        # Click Menu Myinfo
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        time.sleep(1)

        #validasi
        userName = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6").text
        self.assertIn("",userName)
        time.sleep(3)

    def tearDown(self): 
        self.browser.close()
 
if __name__ == "__main__": 
    unittest.main()