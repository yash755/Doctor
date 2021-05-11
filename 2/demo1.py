import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import math

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

file = open('zip.txt','r')

for f in file:
    zip = f
    zip = zip.replace('\n','')

    print (zip)



    mail_url = 'https://www.aligntech.es/en/Find-Invisalign-Doctor/Pages/Search.aspx#v=results&z=' + str(zip) + '&a=&n=&c=&t=adult&cy=es&pr=0&s=e&it=0&lt=&ln=&rd='
    print (mail_url)


    driver.get(mail_url)



    time.sleep(2)

    try:

        WebDriverWait(driver, 2).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    except:
        m = 0


    html2 = driver.page_source
    html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")


    try:
        count = html.find('div',{'id':'dlMapHeaderLabel'})
        count = count.text.strip()

        count = count.split('Invisalign')

        if len(count) >=1:
            count = count[0]
            count = count.replace('Se muestran','')

            count = int(count)

            pages = math.ceil(count/10)
            page_no = 0

            # while page_no < pages:
            base_url = 'https://www.aligntech.es/en/Find-Invisalign-Doctor/Pages/Search.aspx#v=results&z=' + str(zip) + '&a=&n=&c=&t=adult&cy=es&pr=' + str(pages-1) + '&s=e&it=0&lt=&ln=&rd='
            print (base_url)

            driver.get(base_url)

            time.sleep(2)

            html4 = driver.page_source
            html5 = BeautifulSoup(html4, "lxml", from_encoding="utf-8")

            ul = html5.find('ul',{'id':'dlResultList'})

            lis = ul.find_all('li')

            if len(lis) > 0:
                print ("Length" + str(len(lis)))
                for li in lis:
                    id = li.get('id')

                    id = id.replace('dlRow','')

                    name = ''

                    try:
                        name = li.find('span',{'class':'dlFullName'})
                        name = name.text.strip()

                    except:
                        print ("error")

                    name_file = open('name.txt', 'a+')
                    name_file.write(str(zip) + '===' + str(id) + '===' + str(name) + '\n')
                    name_file.close()

            else:
                error = open('error.txt', 'a+')
                error.write(f)
                error.close()

        else:
            error = open('error.txt', 'a+')
            error.write(f)
            error.close()

    except:
        error = open('error.txt', 'a+')
        error.write(f)
        error.close()
              # page_no = page_no + 1



