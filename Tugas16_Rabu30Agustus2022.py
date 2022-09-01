import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin16") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin16@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin16") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', text_atas)
        self.assertEqual(text_bawah, 'created user!')

# ====================  NEGATIF CASE NULL USERNAME, EMAIL, AND PASSWORD ===============================

    def test_b_failed_register_by_username_null(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin13@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin13") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

        # self.assertIn('Email/Username/Password tidak boleh kosong', text_atas)
        # self.assertEqual(text_bawah, 'gagal register!')

    def test_c_failed_register_by_email_null(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin13") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin13") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

        # self.assertIn('Email/Username/Password tidak boleh kosong', text_atas)
        # self.assertEqual(text_bawah, 'gagal register!')

    def test_d_failed_register_by_password_null(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin13") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin13@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

        # self.assertIn('Email/Username/Password tidak boleh kosong', text_atas)
        # self.assertEqual(text_bawah, 'gagal register!')
        

# ====================  NEGATIF CASE MAX INPUT CHARACTER USERNAME, EMAIL, AND PASSWORD ===============================
    
    def test_e_failed_register_by_username_maxinput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15admin15") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin15@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin15") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_f_failed_register_by_email_maxinput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin16") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin16") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')

    def test_g_failed_register_by_password_maxinput(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("admin16") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("admin16@email.com") # isi nama
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16admin16") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', text_atas)
        self.assertEqual(text_bawah, 'Gagal Register!')
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()