#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os


#browser setup
driver = webdriver.Firefox()

"""making url from command line"""

part = ""
for i in sys.argv[1:]:
    part+=i+"+"
part = part[0:-1]
link = "https://www.youtube.com/results?search_query="+part

"""odlazak na link"""

driver.get(link)

"""while petlja koja je True sve dok nije odredjena adresa u pitanju
https://www.google.com/"""
link =""
while(True):
    # ukoliko je odredjena adresa gasi program
    if(driver.current_url=="https://www.google.com/"):
        break
    try:
        # provera trenutnog linka----
        tr_link = driver.current_url
        # ukoliko je link sa watch? i ukoliko != kao neka promenljiva onda ukloni preporuke
        if "watch?v" in tr_link and link!=tr_link:
            link = tr_link
            while (True):
                try:
                    driver.execute_script("document.getElementById('related').remove();")

                    naslov = driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']")
                    driver.execute_script("arguments[0].remove();", naslov)

                    headd = driver.find_element_by_xpath("//title")
                    driver.execute_script("arguments[0].remove();", headd)

                    break
                except:
                    continue
    except:
        continue
#document.body.style.border = "5px solid red";



