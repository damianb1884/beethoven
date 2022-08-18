from curses import KEY_ENTER
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class buscando_beethoven (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Primo\archivos sueltos\Downloads\eeee\TRABAJO\DRIVER\chromedriver.exe")

    def test_1beethoven(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        elemento=driver.find_element_by_name("q")
        elemento.send_keys ("youtube")
        elemento.send_keys (Keys.ENTER)
        time.sleep(3)
        elemento2=driver.find_element_by_class_name("LC20lb MBeuO DKV0Md")
        elemento2.click()
        time.sleep(3)
        elemento3=driver.find_element_by_id("search")
        elemento3.send_keys("beethoven")
        elemento3.send_keys(Keys.ENTER)
        time.sleep(3)
        elemento4=driver.find_element_by_class_name("style-scope ytd-video-renderer")
        elemento4.click()
        time.sleep(30)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()

