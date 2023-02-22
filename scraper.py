#!/usr/bin/env python

from selenium import webdriver
import bs4
import time
import requests
import pandas as pd
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
MASTER_URL = 'https://www.liberation.fr/'
def test_main():
     output_file = open("output.csv","w")
     urls = ['politique/', 'international/', 'checknews/', 'culture/', 'idees-et-debats/', 'societe/', 'enquetes/', 'environnement/', 'economie/']
     for url in urls:
         crawl_link_page(MASTER_URL + url, output_file)
         i = 1
         for i in range(21):
            new_link = MASTER_URL + url + '/' + str(i) + '/' 
            try:
                crawl_link_page(new_link, output_file)
            except Exception as ex: 
                if ex.code == 404:
                    break
            print(i)
     
     output_file.close()

def crawl_link_page(url, output_file):
    # single page chosen from news website
    response = requests.get(url)
    html_doc = response.text

    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    # all text of the article is in p tags
    for article in soup.find_all('article'):
        link = article.a.get('href')
        crawl_article(link, output_file)
     
def crawl_article(link, output_file):
    response = requests.get(MASTER_URL + link)
    html = response.text
    page_soup = bs4.BeautifulSoup(html, 'html.parser')
    paragraphs = page_soup.find_all('p') # class_='CustomContentListItem__Link-sc-2hcki7-2 kPzBgo'
    #for paragraph in paragraphs:
      #  output_file.write(paragraph.get_text())



test_main()
