#!/usr/bin/env python
import bs4
import requests
import pandas as pd
import requests

cookies = {
    '_sp_v1_uid': '1:908:c939bc06-b2cf-493e-ad57-9b269e94599a',
    '_sp_v1_ss': '1:H4sIAAAAAAAAAItWqo5RKimOUbKKBjLyQAyD2lidGKVUEDOvNCcHyC4BK6iurVWKBQAW54XRMAAAAA%3D%3D',
    '_sp_su': 'false',
    'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22efe363e0-5a0d-4171-a3c2-0f3995a6a4de%22%2C%22options%22%3A%7B%22end%22%3A%222024-03-05T00%3A55%3A32.408Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    '_gcl_au': '1.1.1268127049.1675299335',
    'BOOMR_CONSENT': '"opted-in"',
    'consentUUID': 'ad77130a-71b2-43b2-9b71-c0e62b546eaf_16',
    '_gaexp': 'GAX1.2.UL5-1NB-SAmm4B8OsJbesg.19463.1',
    '_fbp': 'fb.1.1675299335388.1803437632',
    'ownpage_fp2': 'd39d93220f9f2d0a',
    '_hjSessionUser_2925396': 'eyJpZCI6IjYzODRlNzZhLTUxNjAtNTI1Zi1hYTdhLWJiZWIyYWJlNDQ2ZCIsImNyZWF0ZWQiOjE2NzUyOTkzMzU0NjksImV4aXN0aW5nIjp0cnVlfQ==',
    '_cc_id': 'b10a4329fef95c7abfbb0040ce603054',
    'panoramaId': '459504da50ac1ef003b68a19c30516d539381e7e20895dd0a42a50b59c59e418',
    '_pubcid': 'a61cd035-3bc6-4a2b-8261-8ea5f3955ee1',
    '_lr_env_src_ats': 'false',
    '__gads': 'ID=00f8473b477634c5:T=1677019295:S=ALNI_MYvO5Vy_a6a5PClAL-kQPf4rCAInw',
    'pbjs-unifiedid': '%7B%22TDID%22%3A%2255da5f0e-b915-4aa4-9223-170ee05f1751%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-02-21T17%3A04%3A20%22%7D',
    'panoramaId_expiry': '1680023060649',
    'authId': '18e800df6c5a02e7b0c614e81642a8b1866b0cbf1824218e9ab155ee163deb03',
    'entitlementsAccessToken': 'uqcA5hYSIWSkcZZ6HllV3g==',
    'libe_device_id': 'e0f845c6-d8b1-462f-ae54-3c4980cdda38',
    'nb_vue_paywall': '9',
    'sqd_vst': '6',
    '_pbjs_userid_consent_data': '3524755945110770',
    'cto_bundle': 'w-MwVl9jNGZ5JTJGSmMlMkJFMDZzMkdybG54eTVyNHpvOTElMkZTUmRIR1FTMjhkRUo0Q1NOZGpTMWNpNEUzTyUyQlVWeDNVV0hmNVRSZm5VcEZSSmY4eG1FalJzVDNOUXY3b0FLc1FTREk5cnNxVVp4N1MzZVFVMUowMW9XTllJSVFWMlBKc0R1YSUyRnN1dE03eEFDNk9mOVlTNkRPT0UyJTJCWmclM0QlM0Q',
    'cto_bidid': '1tdq5l9ySkFaJTJGMEFnVzJScHVIS2Vtd1k5c2JybGRTSm9yTkolMkZpY0YlMkJyYSUyQmUxZUJnOHJXUExCQ0ZzMFFsTnh1RHBMQWppdUVOeGNrSk44OTl5aVhTNWtsRllEMGF1Vlp2JTJCdkR2NnJ6VWpsSXRLT3clM0Q',
    '_parrable_id': 'filteredUntil%253A1679610339%252CfilterHits%253A0',
    '__gpi': 'UID=000009b9fb0b3658:T=1677019295:RT=1679523939:S=ALNI_Mbxh1OVNDVUdbvj3cwIioQZ4ak_2w',
    '_hjIncludedInSessionSample_2925396': '0',
    '_hjSession_2925396': 'eyJpZCI6ImYwMzBmNjA5LTFiZGEtNGVmZi1iN2Q3LTdhY2Q3NzAyNTgwZSIsImNyZWF0ZWQiOjE2Nzk5Mjk4NjI4NjgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    '_sp_v1_data': '2:553698:1675299332:0:87:0:87:0:0:_:-1',
    'atauthority': '%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222024-04-27T15%3A12%3A21.597Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    'libe_event': 'login',
    'accessToken': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImViT3AwR05RSFg1a0ZaaGJ0RUpXaCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubGliZXJhdGlvbi5mci8iLCJzdWIiOiJhdXRoMHw2NDFiMTJjYmRjNDJkZTFiMmMwNTNiY2QiLCJhdWQiOlsiaHR0cHM6Ly9saWJlcmF0aW9uLmZyIiwiaHR0cHM6Ly9saWJlcmF0aW9uLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk5Mjk5NDEsImV4cCI6MTY4MDAxNjM0MSwiYXpwIjoiclhjVXZPRm14bTZxamZWNTQ1U3dPRVNJc1d2TGZEdHUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.hiqE6OiOdHfQvwBnnJSqxOeD_sjxyer4adTyTZnVakV14D5pwraULNppthIfKDy-m-w1gWbol65acPV4ciCRPZjkPXfBhH_If_TFzW6LughkjANSftKvk8Rxgvx6d17OwX2uSXYWy_aISE-PjcvxGgofQzkQQbUGLTzXAxQHWBbW6Bw_EwJyAf8yhDgDMPX0x9wC49As7f25bSFA4EYwG35o_Y5eawrsEFFM1-edypop6pBStLmHAp2MnqUTnArqeGklbVtv9IIOlnvzlVaDHN83DrGNqgm8ct7wYrMQ5HoQ0NbEXzQ2gEwD2SzTAWsYQoDyzSNPtMqQ6i4OdaGF7A',
    'djazsession': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImViT3AwR05RSFg1a0ZaaGJ0RUpXaCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubGliZXJhdGlvbi5mci8iLCJzdWIiOiJhdXRoMHw2NDFiMTJjYmRjNDJkZTFiMmMwNTNiY2QiLCJhdWQiOlsiaHR0cHM6Ly9saWJlcmF0aW9uLmZyIiwiaHR0cHM6Ly9saWJlcmF0aW9uLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk5Mjk5NDEsImV4cCI6MTY4MDAxNjM0MSwiYXpwIjoiclhjVXZPRm14bTZxamZWNTQ1U3dPRVNJc1d2TGZEdHUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.hiqE6OiOdHfQvwBnnJSqxOeD_sjxyer4adTyTZnVakV14D5pwraULNppthIfKDy-m-w1gWbol65acPV4ciCRPZjkPXfBhH_If_TFzW6LughkjANSftKvk8Rxgvx6d17OwX2uSXYWy_aISE-PjcvxGgofQzkQQbUGLTzXAxQHWBbW6Bw_EwJyAf8yhDgDMPX0x9wC49As7f25bSFA4EYwG35o_Y5eawrsEFFM1-edypop6pBStLmHAp2MnqUTnArqeGklbVtv9IIOlnvzlVaDHN83DrGNqgm8ct7wYrMQ5HoQ0NbEXzQ2gEwD2SzTAWsYQoDyzSNPtMqQ6i4OdaGF7A',
    'cdnSecure': 'authenticated.premium.1679937142.a+fYEjn5N0aTe8D/1ZWDkUA0Nhl3Y7jBoCpq5HTfkTY=',
}

headers = {
    'authority': 'www.liberation.fr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_sp_v1_uid=1:908:c939bc06-b2cf-493e-ad57-9b269e94599a; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKBjLyQAyD2lidGKVUEDOvNCcHyC4BK6iurVWKBQAW54XRMAAAAA%3D%3D; _sp_su=false; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22efe363e0-5a0d-4171-a3c2-0f3995a6a4de%22%2C%22options%22%3A%7B%22end%22%3A%222024-03-05T00%3A55%3A32.408Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _gcl_au=1.1.1268127049.1675299335; BOOMR_CONSENT="opted-in"; consentUUID=ad77130a-71b2-43b2-9b71-c0e62b546eaf_16; _gaexp=GAX1.2.UL5-1NB-SAmm4B8OsJbesg.19463.1; _fbp=fb.1.1675299335388.1803437632; ownpage_fp2=d39d93220f9f2d0a; _hjSessionUser_2925396=eyJpZCI6IjYzODRlNzZhLTUxNjAtNTI1Zi1hYTdhLWJiZWIyYWJlNDQ2ZCIsImNyZWF0ZWQiOjE2NzUyOTkzMzU0NjksImV4aXN0aW5nIjp0cnVlfQ==; _cc_id=b10a4329fef95c7abfbb0040ce603054; panoramaId=459504da50ac1ef003b68a19c30516d539381e7e20895dd0a42a50b59c59e418; _pubcid=a61cd035-3bc6-4a2b-8261-8ea5f3955ee1; _lr_env_src_ats=false; __gads=ID=00f8473b477634c5:T=1677019295:S=ALNI_MYvO5Vy_a6a5PClAL-kQPf4rCAInw; pbjs-unifiedid=%7B%22TDID%22%3A%2255da5f0e-b915-4aa4-9223-170ee05f1751%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-02-21T17%3A04%3A20%22%7D; panoramaId_expiry=1680023060649; authId=18e800df6c5a02e7b0c614e81642a8b1866b0cbf1824218e9ab155ee163deb03; entitlementsAccessToken=uqcA5hYSIWSkcZZ6HllV3g==; libe_device_id=e0f845c6-d8b1-462f-ae54-3c4980cdda38; nb_vue_paywall=9; sqd_vst=6; _pbjs_userid_consent_data=3524755945110770; cto_bundle=w-MwVl9jNGZ5JTJGSmMlMkJFMDZzMkdybG54eTVyNHpvOTElMkZTUmRIR1FTMjhkRUo0Q1NOZGpTMWNpNEUzTyUyQlVWeDNVV0hmNVRSZm5VcEZSSmY4eG1FalJzVDNOUXY3b0FLc1FTREk5cnNxVVp4N1MzZVFVMUowMW9XTllJSVFWMlBKc0R1YSUyRnN1dE03eEFDNk9mOVlTNkRPT0UyJTJCWmclM0QlM0Q; cto_bidid=1tdq5l9ySkFaJTJGMEFnVzJScHVIS2Vtd1k5c2JybGRTSm9yTkolMkZpY0YlMkJyYSUyQmUxZUJnOHJXUExCQ0ZzMFFsTnh1RHBMQWppdUVOeGNrSk44OTl5aVhTNWtsRllEMGF1Vlp2JTJCdkR2NnJ6VWpsSXRLT3clM0Q; _parrable_id=filteredUntil%253A1679610339%252CfilterHits%253A0; __gpi=UID=000009b9fb0b3658:T=1677019295:RT=1679523939:S=ALNI_Mbxh1OVNDVUdbvj3cwIioQZ4ak_2w; _hjIncludedInSessionSample_2925396=0; _hjSession_2925396=eyJpZCI6ImYwMzBmNjA5LTFiZGEtNGVmZi1iN2Q3LTdhY2Q3NzAyNTgwZSIsImNyZWF0ZWQiOjE2Nzk5Mjk4NjI4NjgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _sp_v1_data=2:553698:1675299332:0:87:0:87:0:0:_:-1; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222024-04-27T15%3A12%3A21.597Z%22%2C%22path%22%3A%22%2F%22%7D%7D; libe_event=login; accessToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImViT3AwR05RSFg1a0ZaaGJ0RUpXaCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubGliZXJhdGlvbi5mci8iLCJzdWIiOiJhdXRoMHw2NDFiMTJjYmRjNDJkZTFiMmMwNTNiY2QiLCJhdWQiOlsiaHR0cHM6Ly9saWJlcmF0aW9uLmZyIiwiaHR0cHM6Ly9saWJlcmF0aW9uLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk5Mjk5NDEsImV4cCI6MTY4MDAxNjM0MSwiYXpwIjoiclhjVXZPRm14bTZxamZWNTQ1U3dPRVNJc1d2TGZEdHUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.hiqE6OiOdHfQvwBnnJSqxOeD_sjxyer4adTyTZnVakV14D5pwraULNppthIfKDy-m-w1gWbol65acPV4ciCRPZjkPXfBhH_If_TFzW6LughkjANSftKvk8Rxgvx6d17OwX2uSXYWy_aISE-PjcvxGgofQzkQQbUGLTzXAxQHWBbW6Bw_EwJyAf8yhDgDMPX0x9wC49As7f25bSFA4EYwG35o_Y5eawrsEFFM1-edypop6pBStLmHAp2MnqUTnArqeGklbVtv9IIOlnvzlVaDHN83DrGNqgm8ct7wYrMQ5HoQ0NbEXzQ2gEwD2SzTAWsYQoDyzSNPtMqQ6i4OdaGF7A; djazsession=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImViT3AwR05RSFg1a0ZaaGJ0RUpXaCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubGliZXJhdGlvbi5mci8iLCJzdWIiOiJhdXRoMHw2NDFiMTJjYmRjNDJkZTFiMmMwNTNiY2QiLCJhdWQiOlsiaHR0cHM6Ly9saWJlcmF0aW9uLmZyIiwiaHR0cHM6Ly9saWJlcmF0aW9uLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2Nzk5Mjk5NDEsImV4cCI6MTY4MDAxNjM0MSwiYXpwIjoiclhjVXZPRm14bTZxamZWNTQ1U3dPRVNJc1d2TGZEdHUiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIn0.hiqE6OiOdHfQvwBnnJSqxOeD_sjxyer4adTyTZnVakV14D5pwraULNppthIfKDy-m-w1gWbol65acPV4ciCRPZjkPXfBhH_If_TFzW6LughkjANSftKvk8Rxgvx6d17OwX2uSXYWy_aISE-PjcvxGgofQzkQQbUGLTzXAxQHWBbW6Bw_EwJyAf8yhDgDMPX0x9wC49As7f25bSFA4EYwG35o_Y5eawrsEFFM1-edypop6pBStLmHAp2MnqUTnArqeGklbVtv9IIOlnvzlVaDHN83DrGNqgm8ct7wYrMQ5HoQ0NbEXzQ2gEwD2SzTAWsYQoDyzSNPtMqQ6i4OdaGF7A; cdnSecure=authenticated.premium.1679937142.a+fYEjn5N0aTe8D/1ZWDkUA0Nhl3Y7jBoCpq5HTfkTY=',
    'referer': 'https://connexion.liberation.fr/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'redirected': '1',
}

#response = requests.get('https://www.liberation.fr/sciences/', params=params, cookies=cookies, headers=headers)

#response = requests.get('https://www.liberation.fr/sciences/', params=params, cookies=cookies, headers=headers)

#print(response.url)
MASTER_URL = 'https://www.liberation.fr'
def test_main():
     tables = []
     i = 1
     crawl_link_page('https://www.liberation.fr/sciences/', tables)
     for i in range(21): #based on liberation website structure
        new_link = MASTER_URL + '/sciences/' + str(i) + '/' 
        print(new_link)
        try:
            crawl_link_page(new_link, tables)
        except Exception as ex: 
            if ex.code == 404:
                break
        print(i)
     df = pd.DataFrame(data=tables)
     df.to_csv('sciences_vf.csv',encoding='utf-8')

def crawl_link_page(url, tables):
    # single page chosen from news website
    
    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    html_doc = response.text

    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    # all text of the article is in p tags
    for article in soup.find_all('article'):
        link =  MASTER_URL + article.a.get('href')
        print(link)
        crawl_article(link, tables)
     
def crawl_article(link, tables):
    response = requests.get(link, params=params, cookies=cookies, headers=headers)
    html = response.text
    page_soup = bs4.BeautifulSoup(html, 'html.parser')
    date = page_soup.find(class_ ="font_xs color_grey margin-xxs-right font_tertiary header-date")
    paragraphs = page_soup.find_all('p') # class_='CustomContentListItem__Link-sc-2hcki7-2 kPzBgo'
    title = page_soup.find('h1')
    page = ""
    for paragraph in paragraphs:
        page += paragraph.get_text()
        #print (paragraph.get_text()
    row = [date, title, page]
    tables.append(row)



test_main()
