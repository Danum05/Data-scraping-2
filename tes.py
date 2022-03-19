from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import urllib.request
import json
import datetime

service = Service("D:\data scraping 2\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.imdb.com/chart/moviemeter/")

filmList = []
i = 1
while i<=100:
    for film in driver.find_elements(By.TAG_NAME,"tr"):
        print(film.text.split("\n"))
        for img in film.find_elements(By.TAG_NAME,"img"):
            print(img.get_attribute("src"))
            #urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            now = datetime.datetime.now()
            filmList.append(
                {"Ranking": film.text.split("\n")[1].split(' ')[0],
                 "Judul": film.text.split("\n")[0].split(' (')[0],
                 "Tahun_Rilis": film.text.split("\n")[0].split('(')[1].split(')')[0],
                 #"Rating": film.text.split("\n")[2],
                 "Image": img.get_attribute("src"),
                 "Waktu_Scraping": now.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
    break;

hasil_scraping = open("hasilscraping.json","w")
json.dump(filmList, hasil_scraping, indent = 6)

driver.quit()
