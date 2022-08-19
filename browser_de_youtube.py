#from curses import KEY_ENTER
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class buscando_beethoven (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driver Chrome\chromedriver.exe")

    def test_1beethoven(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        elemento=driver.find_element_by_name("q")
        elemento.send_keys ("youtube")
        elemento.send_keys (Keys.ENTER)
        time.sleep(3)
        
        
        elemento2=driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
        elemento2.click()
        time.sleep(3)
        
        elemento3=driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
        
        elemento3.send_keys("beethoven")
        elemento3.send_keys(Keys.ENTER)
        time.sleep(3)
        elemento4=driver.find_element_by_link_text("Beethoven 🌕 Sonata Claro de Luna (60 Minutos) 🎹 Música Clásica de Piano para Estudiar y Concentrarse")
        elemento4.click()
        time.sleep(30)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()

