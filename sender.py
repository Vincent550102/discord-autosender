# coding=UTF-8
import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()
email = os.getenv('email', default=None)
passwd = os.getenv('passwd', default=None)

sched = BlockingScheduler()


class Crawler():
    def __init__(self):
        self.URL = 'https://discord.com/channels/358942292352040970/577555543049240596'
        self.email = os.getenv('email', default=None)
        self.passwd = os.getenv('passwd', default=None)

    def awake_driver(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        # options.add_argument('--headless')
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.URL)
        sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(self.email)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(self.passwd)
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div').click()

    def run(self):
        self.awake_driver()

        @sched.scheduled_job('interval', minutes=20)
        def timed_job():
            sleep(10)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[1]/div[2]').send_keys('/warp Vincent550102 ??????45???(2/3)???120????????????(1/3)????????????????????????????????????????????????????????????????????????\n')

        sched.start()
        # timed_job()
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
