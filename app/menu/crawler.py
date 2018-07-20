import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time


class BaskinCrawler:

    def __init__(self, name, ice_type, description=None, img=None):
        self.name = name
        self.ice_type = ice_type
        self.img = img
        self.description = description

    @classmethod
    def create_html(cls):
        url = 'https://baskinrobbins.co.kr/menu/list.php?top=A'

        file_path = 'data/ice_cream_list.html'

        driver = webdriver.Chrome('driver/chromedriver')

        driver.get(url)

        time.sleep(2)

        if not os.path.exists(file_path):

            html = driver.page_source

            open(file_path, 'wt').write(html)

        else:
            open(file_path, 'rt').read()

        driver.close()

    @classmethod
    def get_ice_cream_list(cls):
        file_path = 'data/ice_cream_list.html'

        html = open(file_path, 'rt').read()

        soup = BeautifulSoup(html, 'lxml')

        ice_cream_list = []

        ul_contents = soup.select("ul.list li")

        for li in ul_contents:
            content_name = li.select_one('span')
            content_type = li.select_one('div.hashtag li a')

            if content_name is not None and content_type is not None:
                content_instance = BaskinCrawler(
                    name=content_name.text,
                    ice_type=content_type.text,
                    description='공통사항',
                )
                ice_cream_list.append(content_instance)

        for item in ice_cream_list:
            print(item)

    def __str__(self):
        return f'이름: {self.name} / 타입:{self.ice_type} / {self.description}'


BaskinCrawler.get_ice_cream_list()
