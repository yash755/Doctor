import requests
import requests
import json
from bs4 import BeautifulSoup
import xlsxwriter
import re
import csv

workbook = xlsxwriter.Workbook('main_file_1_2.xlsx')
worksheet = workbook.add_worksheet()
line_count = 0


file = open('nam2.txt','r')

for f in file:
    data = f
    data = data.replace('\n','')

    data = data.split('===')

    zipcode = data[0]
    id = data[1]
    doctorname = data[2]

    url = "https://www.aligntech.es/Profile/Details/" + str(doctorname) + "/" +  str(id) +"?locale=es"

    print (url)

    headers = {
        'sec-ch-ua': "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?0",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'sec-fetch-site': "none",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'cache-control': "no-cache",
        'postman-token': "6c8e1c02-6c35-8cf3-0a34-42851ed86e65"
    }

    response = requests.request("GET", url, headers=headers)

    html1 = BeautifulSoup(response.content, 'html.parser')

    try:
        add = html1.find('div',{'class':'col-xs-7'})
        add = str(add)
        add = add.split('<br/>')


        if len(add) == 5:

            credentials = add[1]
            credentials = credentials.strip()
            credentials = credentials.replace('\n','')

            address1 = add[2]
            address2 = add[3]
            phone = add[4].strip()
            phone = phone.replace('\n','')
            phone = phone.replace(' </div>', '')

            email = ''
            website = ''

            links = html1.find_all('a')

            for link in links:
                href = link.get('href')
                linktext = link.text.strip()

                if href and 'mailto' in href:
                    email = linktext

                if 'www' in linktext:
                    website  = linktext

            j = 0
            worksheet.write(line_count, j, url)
            j = j + 1
            worksheet.write(line_count, j, doctorname)
            j = j + 1
            worksheet.write(line_count, j, credentials)
            j = j + 1
            worksheet.write(line_count, j, address1)
            j = j + 1
            worksheet.write(line_count, j, address2)
            j = j + 1
            worksheet.write(line_count, j, phone)
            j = j + 1
            worksheet.write(line_count, j, email)
            j = j + 1
            worksheet.write(line_count, j, website)
            j = j + 1

    except:
        error = open('fie_errir.txt','a+')
        error.write(f)
        error.close()


    line_count = line_count + 1


workbook.close()


