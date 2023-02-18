#!/usr/bin/env python

from selenium import webdriver
import bs4
import time
import requests
import pandas as pd
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#@pytest.mark.skip(reason="Do not run in CI")
def test_driver_manager_chrome():
    #service = ChromeService(executable_path=ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=service)
    
    output_file = open("output.csv","w")
    
    news_url = 'https://www.liberation.fr/idees-et-debats/frederic-gros-dire-que-la-guerre-est-dans-la-nature-humaine-est-un-raisonnement-paresseux-20230217_MAY6BFGAANHW5E3MESNNG5VX5Y/'
    response = requests.get(news_url)
    html_doc = response.text
    soup = bs4.BeautifulSoup(html_doc, "html.parser")

    paragraphs = soup.find_all('p') # class_='CustomContentListItem__Link-sc-2hcki7-2 kPzBgo'
    
    for paragraph in paragraphs:
        output_file.write(paragraph.get_text())

    output_file.close()

    # i = 0
    # for i in range(len(pages)): 
    #      driver.get(url)
    # webpages = driver.find_elements_by_class_name('CustomContentListItem__Article-sc-2hcki7-0 euEONJ')
    # number_of_pages = int(webpages[-2].text)
    # for _ in range(number_of_pages):
    #     next_page = driver.find_element(By.XPATH,"//a[text()='›']").click()
    #     time.sleep(2)
    # driver.quit()
     

# def get_links_from_html(html: str):

#     soup = bs4.BeautifulSoup(html, "html.parser")
#     links = []
#     for table_element in soup.find_all("a"):
#         table = []
#        for tr in table_element.find_all("tr"):
#             row = ["".join(cell.stripped_strings) for cell in tr.find_all(["td", "th"])]
#             table.append(row)
#         tables.append(table)

#     return tables


test_driver_manager_chrome()