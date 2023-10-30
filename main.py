from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR = ""
USERNAME = ""
PASSWORD = ""

class InstaFollow:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(USERNAME)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        input("enter")
        # time.sleep(10)
        # save_info = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_lM"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
        # save_info.click()
        # time.sleep(5)


    def find(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR}")
        time.sleep(5)
        following = self.driver.find_element(By.PARTIAL_LINK_TEXT, "following")
        following.click()
        time.sleep(2)
        model = self.driver.find_element(By.XPATH,
                                         '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel.click()


bot = InstaFollow()
bot.login()
bot.find()
bot.follow()