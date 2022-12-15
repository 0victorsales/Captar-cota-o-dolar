from selenium import webdriver
import time




class youtube:
    def _init_(self):
        self.site_link = "https://www.youtube.com/"
                    
        self.driver = webdriver.Chrome(executable_path="C:\\WebDrivers\\chromedriver.exe")
        self.driver.maximize_window()
    
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.site_link)
        time.sleep(10)



start = youtube()
start.abrir_site()
