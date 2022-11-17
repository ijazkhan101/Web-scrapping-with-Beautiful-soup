# webiste scraping
# use APIs
# HTML web scraping using tool like bs4
# install libraires 
# pip install requests
# pip install bs4
# pip install html5lib

import requests 
from bs4 import BeautifulSoup 


url ='https://www.codewithharry.com'

r = requests.get(url)
htmlContent =r.content
#print(htmlContent)

# step 2
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

# step 3 : HTML  Tree Traversal
title =soup.title 
#print(title)

# get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)
# get all the a from the page
paras = soup.find_all('a')
#print(paras)

#get 1st elment in the html page
print(soup.find_all('p',class_="text-gray-700 text-base dark:text-gray-400"))

# get the text from tags/ soup
print(soup.find('p').get_text())
print(soup.get_text())