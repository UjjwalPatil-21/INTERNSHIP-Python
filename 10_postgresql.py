#To extract the javascript related data from git hub website using python

import requests 
from bs4 import BeautifulSoup

pagelink = 'https://github.com/topics/postgresql?page='

product_no = 30    
allpagesurl =[]
for num in range(1,8):
    allpagesurl.append(pagelink + str(num))


all_dataset_list = []
for val in allpagesurl:
    html_data = requests.get(val).text
    soup_data = BeautifulSoup(html_data,'lxml')
    all_divs = soup_data.find_all('div',class_='d-flex flex-justify-between my-3')

    if(val == allpagesurl[6]):
        product_no = 20      

    for item in all_divs[:product_no]:
        respo_name = item.find('a',class_='text-bold wb-break-word').text
        user_name = item.a.text
        stars=item.find('span',class_='Counter js-social-count')['title']
        weburl = 'https://github.com'
        sub_url=item.find('a',class_='text-bold wb-break-word')['href']
        main_url=weburl+sub_url
        
    

        all_dataset_dict = {
            'Repository Name':respo_name.strip(),
            'Username':user_name.strip(),
            'Stars':stars,
            'URL':main_url
        } 
 
        all_dataset_list.append(all_dataset_dict)
 
 
    import pandas as ps
    df = ps.DataFrame(all_dataset_list)


df.to_excel("postgresql.xlsx")