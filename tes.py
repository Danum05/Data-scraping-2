from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = r"D:\scrapping 2"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://www.metacritic.com/browse/movies/score/metascore/all/filtered/itunes")

now = datetime.now()
albumlist = []
i = 1

while i<=100:
    for album in driver.find_elements_by_tag_name("tr"):
        print(album.text)
        for tag in album.find_elements_by_tag_name("a"):
            for img in tag.find_elements_by_tag_name("img"):
                print(img.get_attribute("src"))
                i = i+1
                albumlist.append(
                    {"Rating": album.text.split("\n")[0],
                     "No": album.text.split("\n")[1],
                     "Judul": album.text.split("\n")[2],
                     "Release": album.text.split("\n")[3],
                     "waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S"),
                     "Image": img.get_attribute("src")
                     }
                )
hasil_scraping = open("scrapping.json", "w")
json.dump(albumlist, hasil_scraping, indent=5)
hasil_scraping.close()

driver.quit()
