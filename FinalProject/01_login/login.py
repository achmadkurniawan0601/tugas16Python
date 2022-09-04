import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO LOGIN

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # 1. valid username and password
    def test_case01(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").text
        self.assertIn('Paul Collings', user)

    # 2. username valid and password invalid
    def test_case02(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin12345") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn('Invalid credentials', user)

    # 3. username invalid and password valid
    def test_case03(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("admins") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text
        self.assertIn('Invalid credentials', user)

    # 4. username null and password valid
    def test_case04(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        self.assertIn('Required', user)

    # 5. username valid and password null
    def test_case05(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        self.assertIn('Required', user)

    # 6. username and password null
    def test_case06(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(2)
        browser.find_element(By.NAME,"username").send_keys("") 
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() 
        time.sleep(1)

        #validasi
        user = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        password = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text

        self.assertIn('Required', user)
        self.assertIn('Required', password)

    def tearDown(self): 
        self.browser.close()
 
if __name__ == "__main__": 
    unittest.main()