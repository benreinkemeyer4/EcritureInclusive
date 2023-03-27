#!/usr/bin/env python
import bs4
import requests
import pandas as pd
import requests

cookies = {
    'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22bb5d222e-ee3a-497b-9a57-4a0d4f8f958a%22%2C%22options%22%3A%7B%22end%22%3A%222024-04-26T23%3A10%3A53.989Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-626664-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_sharedID': '05dfaf1d-0f5e-4cfb-a9fe-a0a7f0d50836',
    'ledevoir-supporte-push-v1': 'true',
    '_gcl_au': '1.1.1953603227.1679872255',
    '_gid': 'GA1.2.1720944217.1679872255',
    '_tfpvi': 'ODZiN2MxMzYtYzFjMC00NTYzLTliZDctNDQxY2I0MTljNmFkIy05LTk%3D',
    'm32_uStorage': '{"Version":"465","Data":{"uuid":"b8b8e4a2-26d6-4246-a9a7-bf2b749c7ed6"}}',
    '_fbp': 'fb.1.1679872254915.610216075',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBWDgBj4B2boIDM3UQCYAnNIAscjoJABfIA',
    '_pcid': '%7B%22browserId%22%3A%22lfq0kfkf7lijovwq%22%7D',
    '__pnahc': '0',
    'ln_or': 'eyIxODUyNDY1IjoiZCJ9',
    'sa-user-id': 's%253A0-0421bdd6-eeb0-4b8a-4e5d-28a1d1b54b1a.TFqEKFDllOPVXN8yCvlF8zX8HZ4Om3mti4IMVZiGaMA',
    'sa-user-id-v2': 's%253ABCG91u6wS4pOXSih0bVLGoy08G0.Ug6LUujS3vwp2An2ycHj1cb%252FtIBi66T5d1RcSpU3kZo',
    '__pat': '-14400000',
    'cX_G': 'cx%3A25yx9ccip6uj729stmulri7cnp%3A3pih3ej3b75we',
    'ledevoir-veut-alertes-v1': 'false',
    '__gads': 'ID=484989caf6c4e91e:T=1679872255:S=ALNI_MaLk6aaIksv01ZIwSW8FgGJn55jHQ',
    '__gpi': 'UID=00000a321e175f04:T=1679872255:RT=1679872255:S=ALNI_MakglzS40wfwVrMHo-LhBCc7zqrTA',
    'm0t1679874333': '1',
    'pw6': 'WyI3ODYyMDgiLCI3ODYwNzUiLCI3ODY3MTYiLCI3ODY2OTEiLCI3ODY2NDMiXQ==',
    'm0t1679875942': '1',
    'm0t1679875972': '1',
    'm0t1679876718': '1',
    'm0t1679876732': '1',
    'm32_sStorage': '01d06108-6224-657f-a37d-e3291b3a930d',
    'm0t1679878311': '1',
    'm0t1679878320': '1',
    'm0t1679878647': '1',
    'm0t1679878655': '1',
    'm32_pubgeo': 'JTdCJTIyaXAlMjIlM0ElMjIxNDAuMTgwLjI0MC4xMjUlMjIlMkMlMjJjb3VudHJ5X2NvZGUlMjIlM0ElMjJVUyUyMiUyQyUyMmNvdW50cnlfbmFtZSUyMiUzQSUyMnVuaXRlZCUyMHN0YXRlcyUyMiUyQyUyMnJlZ2lvbl9jb2RlJTIyJTNBJTIyTkolMjIlMkMlMjJjaXR5JTIyJTNBJTIycHJpbmNldG9uJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MC4zNyUyQyUyMmxvbmdpdHVkZSUyMiUzQS03NC42NyUyQyUyMm1ldHJvJTIyJTNBNTA0JTJDJTIycG9zdGFsX2NvZGUlMjIlM0ElMjIwODU0MCUyMiU3RA==',
    'm0t1679879088': '1',
    'm0t1679879095': '1',
    '_dc_gtm_UA-1157473-1': '1',
    '_gat': '1',
    '_gat_pianoTracker': '1',
    'm0t1679879360': '1',
    '__pvi': 'eyJpZCI6InYtbGZxMGtma2w5YTV0M3B4ciIsImRvbWFpbiI6Ii5sZWRldm9pci5jb20iLCJ0aW1lIjoxNjc5ODc5MzY1MTI0fQ%3D%3D',
    '_ga_7TVJ423H79': 'GS1.1.1679872254.1.1.1679879365.0.0.0',
    '__adblocker': 'false',
    '__tbc': '%7Bkpex%7DIqy-f3fQOW3nEnRS-E63YwD3vYxfSOH9_Hxj9UHrZ677PXOu9G8TaxItVz3CWpr0',
    'xbc': '%7Bkpex%7Du9mrAWM_IYcl1ks_YGT3JzqaBFZNvYN6O6oRX0wbLjCzNCcoHEAon15VqB2sMGdptJ-OQl44vaF0SNUbKuaNpqOuDkVCdWqtcLev4F26N7c46wU0eoIh6kIZthBKnQXqfd21IUiMCXFKLe58igWoJuxtp_OSIcjHRnUIcKh9JO2h_A9NyL3GOMiKxPvXIbdKS-a5oTOM37EHMuZCGM6BQJ23hQmQ7b39HLPZfJ035YVxDdQrczam8DRjCZ-tyR3Zy5_E1AFU13xGpZhmfafPWeIOE7YCZoy-U8XzmrzQu0NKCToElhqAQ67XBkwlvROGpX6GHE3c-aRZEeYwwAdUS2SRejWsLmp9FXpWIiCV6aPKghPS5u6wMj840uDejNLEbOlv_gbQsMsezOnYbTAGh-G7aCRWDxZOHIMVR5-WUSDCD7UxM3br6LqNPSXe50NRYfsO7ZMOjY7NXRRFbN_lAuagp-4Oqo7p-qQYr1awzzFIbhX47PAk9SYOdlM1vJexCAcBMag44TeNp4jDHdgXH_9MErUqz1a1DaDjg2nATI-BW94qdIDu-AznvlVBG_1zvga74_uEhgKZgd0VrfLGs34eYYOzrUP79owfJM0npktXziBOvzeUIxQtQ7CqWN-eY1J4Fl1wwn9gS0TG54PDtKv_adq3Pm_oNmlmK6rUUS5slK_7H5DxNy6-AWntzcRXNuBA7Z12djDjrpH5NkWuXupNQmeecrTtyy8mJot0TKQ',
    '_ga': 'GA1.2.953494394.1679872255',
    'm32_timeOnPageStorage': '{"requestId":"lfq4stol2kf3s1dt","timeOnPage":7559,"Version":"465"}',
    'ledevoir': 'e7cc3f5dd1be967a5e4725e4c735e6f1:6fbbb8cfd038c1aba51b51d0dce8afed38180f17',
    'devoir_auto': 'WyJmaTF2ODBzbzNucGx6cGh3enhhcjZzYWIwaDE4YXpteCIsImJycjJAcHJpbmNldG9uLmVkdSJd',
    'devoir_profil': 'WyIwIiwiIiwiIiwiN2EyOWZkODU0ZmE5NTIxNzg1ODlkZmI3NDc3ZjMzOTZiNGQwMDAyZDNhNDIyODQyYzQ4YzliMjc4NTNiOGJkOCJd',
}

headers = {
    'authority': 'www.ledevoir.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22bb5d222e-ee3a-497b-9a57-4a0d4f8f958a%22%2C%22options%22%3A%7B%22end%22%3A%222024-04-26T23%3A10%3A53.989Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-626664-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; _pbjs_userid_consent_data=3524755945110770; _sharedID=05dfaf1d-0f5e-4cfb-a9fe-a0a7f0d50836; ledevoir-supporte-push-v1=true; _gcl_au=1.1.1953603227.1679872255; _gid=GA1.2.1720944217.1679872255; _tfpvi=ODZiN2MxMzYtYzFjMC00NTYzLTliZDctNDQxY2I0MTljNmFkIy05LTk%3D; m32_uStorage={"Version":"465","Data":{"uuid":"b8b8e4a2-26d6-4246-a9a7-bf2b749c7ed6"}}; _fbp=fb.1.1679872254915.610216075; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBWDgBj4B2boIDM3UQCYAnNIAscjoJABfIA; _pcid=%7B%22browserId%22%3A%22lfq0kfkf7lijovwq%22%7D; __pnahc=0; ln_or=eyIxODUyNDY1IjoiZCJ9; sa-user-id=s%253A0-0421bdd6-eeb0-4b8a-4e5d-28a1d1b54b1a.TFqEKFDllOPVXN8yCvlF8zX8HZ4Om3mti4IMVZiGaMA; sa-user-id-v2=s%253ABCG91u6wS4pOXSih0bVLGoy08G0.Ug6LUujS3vwp2An2ycHj1cb%252FtIBi66T5d1RcSpU3kZo; __pat=-14400000; cX_G=cx%3A25yx9ccip6uj729stmulri7cnp%3A3pih3ej3b75we; ledevoir-veut-alertes-v1=false; __gads=ID=484989caf6c4e91e:T=1679872255:S=ALNI_MaLk6aaIksv01ZIwSW8FgGJn55jHQ; __gpi=UID=00000a321e175f04:T=1679872255:RT=1679872255:S=ALNI_MakglzS40wfwVrMHo-LhBCc7zqrTA; m0t1679874333=1; pw6=WyI3ODYyMDgiLCI3ODYwNzUiLCI3ODY3MTYiLCI3ODY2OTEiLCI3ODY2NDMiXQ==; m0t1679875942=1; m0t1679875972=1; m0t1679876718=1; m0t1679876732=1; m32_sStorage=01d06108-6224-657f-a37d-e3291b3a930d; m0t1679878311=1; m0t1679878320=1; m0t1679878647=1; m0t1679878655=1; m32_pubgeo=JTdCJTIyaXAlMjIlM0ElMjIxNDAuMTgwLjI0MC4xMjUlMjIlMkMlMjJjb3VudHJ5X2NvZGUlMjIlM0ElMjJVUyUyMiUyQyUyMmNvdW50cnlfbmFtZSUyMiUzQSUyMnVuaXRlZCUyMHN0YXRlcyUyMiUyQyUyMnJlZ2lvbl9jb2RlJTIyJTNBJTIyTkolMjIlMkMlMjJjaXR5JTIyJTNBJTIycHJpbmNldG9uJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MC4zNyUyQyUyMmxvbmdpdHVkZSUyMiUzQS03NC42NyUyQyUyMm1ldHJvJTIyJTNBNTA0JTJDJTIycG9zdGFsX2NvZGUlMjIlM0ElMjIwODU0MCUyMiU3RA==; m0t1679879088=1; m0t1679879095=1; _dc_gtm_UA-1157473-1=1; _gat=1; _gat_pianoTracker=1; m0t1679879360=1; __pvi=eyJpZCI6InYtbGZxMGtma2w5YTV0M3B4ciIsImRvbWFpbiI6Ii5sZWRldm9pci5jb20iLCJ0aW1lIjoxNjc5ODc5MzY1MTI0fQ%3D%3D; _ga_7TVJ423H79=GS1.1.1679872254.1.1.1679879365.0.0.0; __adblocker=false; __tbc=%7Bkpex%7DIqy-f3fQOW3nEnRS-E63YwD3vYxfSOH9_Hxj9UHrZ677PXOu9G8TaxItVz3CWpr0; xbc=%7Bkpex%7Du9mrAWM_IYcl1ks_YGT3JzqaBFZNvYN6O6oRX0wbLjCzNCcoHEAon15VqB2sMGdptJ-OQl44vaF0SNUbKuaNpqOuDkVCdWqtcLev4F26N7c46wU0eoIh6kIZthBKnQXqfd21IUiMCXFKLe58igWoJuxtp_OSIcjHRnUIcKh9JO2h_A9NyL3GOMiKxPvXIbdKS-a5oTOM37EHMuZCGM6BQJ23hQmQ7b39HLPZfJ035YVxDdQrczam8DRjCZ-tyR3Zy5_E1AFU13xGpZhmfafPWeIOE7YCZoy-U8XzmrzQu0NKCToElhqAQ67XBkwlvROGpX6GHE3c-aRZEeYwwAdUS2SRejWsLmp9FXpWIiCV6aPKghPS5u6wMj840uDejNLEbOlv_gbQsMsezOnYbTAGh-G7aCRWDxZOHIMVR5-WUSDCD7UxM3br6LqNPSXe50NRYfsO7ZMOjY7NXRRFbN_lAuagp-4Oqo7p-qQYr1awzzFIbhX47PAk9SYOdlM1vJexCAcBMag44TeNp4jDHdgXH_9MErUqz1a1DaDjg2nATI-BW94qdIDu-AznvlVBG_1zvga74_uEhgKZgd0VrfLGs34eYYOzrUP79owfJM0npktXziBOvzeUIxQtQ7CqWN-eY1J4Fl1wwn9gS0TG54PDtKv_adq3Pm_oNmlmK6rUUS5slK_7H5DxNy6-AWntzcRXNuBA7Z12djDjrpH5NkWuXupNQmeecrTtyy8mJot0TKQ; _ga=GA1.2.953494394.1679872255; m32_timeOnPageStorage={"requestId":"lfq4stol2kf3s1dt","timeOnPage":7559,"Version":"465"}; ledevoir=e7cc3f5dd1be967a5e4725e4c735e6f1:6fbbb8cfd038c1aba51b51d0dce8afed38180f17; devoir_auto=WyJmaTF2ODBzbzNucGx6cGh3enhhcjZzYWIwaDE4YXpteCIsImJycjJAcHJpbmNldG9uLmVkdSJd; devoir_profil=WyIwIiwiIiwiIiwiN2EyOWZkODU0ZmE5NTIxNzg1ODlkZmI3NDc3ZjMzOTZiNGQwMDAyZDNhNDIyODQyYzQ4YzliMjc4NTNiOGJkOCJd',
    'referer': 'https://www.ledevoir.com/auth/login',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}



MASTER_URL = 'https://www.ledevoir.com'
def test_main():
     tables = []
     response = requests.get('https://www.ledevoir.com/vivre', cookies=cookies, headers=headers)
     print(response)
     crawl_link_page('https://www.ledevoir.com/vivre', tables)
     for i in range(2, 50): #based on liberation website structure
        new_link = MASTER_URL + '/vivre?page=' + str(i) 
        print(new_link)
        try:
            crawl_link_page(new_link, tables)
        except Exception as ex: 
            if ex.code == 404:
                break
        print(i)
     df = pd.DataFrame(data=tables)
     df.to_csv('ledevoir_vivre.csv',encoding='utf-8')

def crawl_link_page(url, tables):
    # single page chosen from news website
    response = requests.get(url, cookies=cookies, headers=headers)
    print(response.url)
    html_doc = response.text

    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    # all text of the article is in p tags
    #print(soup.find_all("article", {"class": "article-box"}))
    for article in soup.find_all("article", {"class": "article-horizontal"}):
        link = article.a.get('href')
        if "interactif" in link or "special" in link:
            continue
        else:
            link = MASTER_URL + link
            crawl_article(link, tables)
     
def crawl_article(link, tables):
    response = requests.get(link, cookies=cookies, headers=headers)
    print(response.url)
    html = response.text

    page_soup = bs4.BeautifulSoup(html, 'html.parser')
    try:
        date_x = page_soup.find("time")
        date = date_x.get_text()
    except Exception as ex:
        date = ''
    
    
    
    paragraphs = page_soup.find_all('p') # class_='CustomContentListItem__Link-sc-2hcki7-2 kPzBgo'
    title = page_soup.find('h1').get_text()
    page = ""
    for paragraph in paragraphs:
        page += paragraph.get_text()
        #print(paragraph.get_text())
    row = [date, title, page]

    tables.append(row)



test_main()
