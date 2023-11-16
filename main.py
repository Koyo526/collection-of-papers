import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import re



url  = 'https://www.semanticscholar.org/paper/Plasma-%3A-Scalable-Autonomous-Smart-Contracts-Poon/cbc775e301d62740bcb3b8ec361721b3edd7c879'
res = requests.get(url)
print(res.status_code)
print(res.encoding)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
title_text = soup.find('title').get_text()
print("Title: "+title_text)

"""
s = Citations.find_all(class_="paper-nav__nav-label")
print(s)
#result = re.sub(r"\D", "", s)
"""



citation_titles=[]
title_links = []
Citation_number = 0
Citation_URL_number = 0
for i in range(1,30):
    try:
        print(i)
        #入力はここのURLを変えてください
        url = 'https://www.semanticscholar.org/paper/Plasma-%3A-Scalable-Autonomous-Smart-Contracts-Poon/cbc775e301d62740bcb3b8ec361721b3edd7c879'
        url = url + "?sort=relevance&page=" + str(i)
        #print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        Citations = soup.find(class_= "citation-list__citations")

        #Getting Citation paper titles
        #print(len(Citations.find_all(class_="cl-paper-title")))
        Citation_number = Citation_number + len(Citations.find_all(class_="cl-paper-title"))
        for Citation_title in Citations.find_all(class_="cl-paper-title"):
            try:
                citation_titles.append(Citation_title.text)
            except:
                pass
        #print(citation_titles)

        #Getting Citation title URL
        get_link = Citations.find_all('a',attrs={'class':''})
        #print(len(get_link))
        Citation_URL_number = Citation_URL_number + len(get_link)
        for i in range(len(get_link)):
            try:
                link_ = get_link[i].get("href")
                link_ = "https://www.semanticscholar.org" + link_
                title_links.append(link_)
            except:
                pass
        #print(title_links)


    except:
        pass


print(citation_titles)
print(title_links)
print(Citation_number)
print(Citation_URL_number)
#title_link_list = [citation_titles,title_links]
d = {"Title":citation_titles,"Link":title_links}

df = pd.DataFrame(d)
print(df)
df.to_csv("Citation_list.csv")
