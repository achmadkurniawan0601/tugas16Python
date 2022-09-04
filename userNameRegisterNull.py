import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
        def test_b_failed_register_by_usernamenull(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("testerqa@email.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerqa") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Email/Username/Password tidak boleh kosong', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()