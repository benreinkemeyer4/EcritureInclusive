#!/usr/bin/env python
import bs4
import requests
import pandas as pd
import requests

cookies = {
    'G_AUTH2_MIGRATION': 'informational',
    'critical-css-home': '71277d09197ab98bd4ce753985a5c8d9',
    'euconsent-v2': 'CPpIRAAPpIRAAFzABBFRC8CsAP_AAH_AAAqIJTNf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7_______________________________________________________________________-8EmwCTDVuIAuxLHAm2jCKBECMKwkKoFABRQDC0QGEDq4KdlcBPrCJAAgFAEYEQIcAUYMAgAAAgCQiICQI8EAgAIgEAAIAFQiEABGwCCgAsBAIABQDQsUYoAhAkIMiIiKUwICJEgoJ7KhBKD_Q0whDrLACg0f8VCAiUAIVgRCQsHIcESAl4skCzFG-QAjACgFEqFagk9NAAA',
    'lmd_consent': '%7B%22userId%22%3A%2277b3ced3-8768-49d6-956c-537e94efc623%22%2C%22timestamp%22%3A%221679673149.253987654%22%2C%22version%22%3A1%2C%22cmpId%22%3A371%2C%22displayMode%22%3A%22standard%22%2C%22purposes%22%3A%7B%22analytics%22%3Atrue%2C%22ads%22%3Atrue%2C%22personalization%22%3Atrue%2C%22mediaPlatforms%22%3Atrue%2C%22social%22%3Atrue%7D%7D',
    'atauthority': '%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22default%22%2C%22visitor_mode%22%3A%22optin%22%7D%2C%22options%22%3A%7B%22end%22%3A%222024-04-24T15%3A52%3A29.387Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    '_fbp': 'fb.1.1679673149496.873904607',
    '_gcl_au': '1.1.1482063594.1679673150',
    '_cb': 'CDU-k-Cvm3NkCmnsKH',
    'uid_dm': '4ebaeb2d-631b-bfa8-7ece-83399c950a06',
    'lead': '2aadc901-aee7-4a24-b62a-8a71036b14df',
    '__gads': 'ID=16e428f4526358ae-2208f935e4de00e6:T=1679673149:S=ALNI_MZ_9gCd-6YfH7c6PrV8xQjfqzUjWQ',
    'obs_ab_v2': '%7B%22paywall_length%22%3A%5B%22450%22%2C%22desktop%22%2C%22index%22%5D%7D',
    'critical-css-article-v2': '71277d09197ab98bd4ce753985a5c8d9',
    'JSESSIONID': '45a125b91ec12c37ef00e9414977',
    'lobs_thruTunnel': 'true',
    '_tt_enable_cookie': '1',
    '_ttp': 'vieyxujSHc1c9nVXqdYqAeoki_v',
    'm_ses': '20230324120101',
    'm_cnt': '3',
    'sbt_i': '5NzQzLWZhMGZjMGJhNmY1NTs7Njc3Y2M2ZjAtNDE2ZC00M2U4LTlmYmMtNzRlNmNiMmVhMTFhOzMDM3ZWY4OTgtYTE5NS00NWZiLWE0Y2EtZGIxM2QyMzBiNDgzOzM2M2M4MmM4LWYzYTAtNDg3ZC0A=',
    'lmd_cap': '_o1fsq189k',
    'lobsNLPolitique': '2023-3-24*2',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-561552-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    'lobs_sc_cntr': 'Ma9qE9eFEP0ONTfPlGwZXkpIw08%3D',
    'g_state': '{"i_p":1680379922776,"i_l":3}',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-561552-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    'lobs_inscrits_1-counter': '20230308.OBS70477%2C20230324.OBS71311%2C20230324.OBS71326%2C20230322.OBS71232%2C20221107.OBS65629%2C20221106.OBS65566%2C20230323.OBS71272%2C20230314.OBS70789%2C20230315.OBS70894%2C20230309.OBS70581%2C20230321.OBS71185%2C20230321.OBS71176%2C20230322.OBS71186%2C20230325.OBS71360%2C20230325.OBS71345%2C20230206.OBS69226',
    'lastAboTeaser': '20230324.OBS71311_Retraites_Et_Si_Emmanuel_Macron_S_Offrait_Une_Porte_De_Sortie_Avec_L_Article_10_De_La_Constitution',
    'lobs_inscrits_1': 'Qp8d8wzB0GiGINauXRdnK7lKRm0%2B8OiS',
    '_cb_svref': 'null',
    '__gpi': 'UID=00000a2faa8c98d6:T=1679673149:RT=1679842002:S=ALNI_Ma4tBJfmtxoMg0glxcQx1UpF0ACQQ',
    'cto_bundle': 'RiYcjF9hYklxY2lzQWdvSUc2WSUyRjQycUNrYlVHNXR1Z2VCa1BhVmpZOVg4YlladjJoZjhNRndZdiUyQnp1TGRKMk1oWFBSTGMwNSUyRnBQd1VIU3BQVHpPZHltT0lta0ZMM1QxTUFhMmx2cWtNek1uT1J1dnFrbmNaVFc4SXpvNEJjc1dBcEJCQ1NXa0tJSWk2eFlBU1UlMkJnd2ltWiUyQjNJQkI1bURFQVBmbE9NdGFETDNUOTRoR1N5Q0NFYmZqOEs1blQ0TWNYR1NqUUUlMkZieTdBVWclMkJtSVZKWkoxV0tzOEElM0QlM0Q',
    '_chartbeat2': '.1675788051481.1679842062322.0000000000000111.maabfBemdtYBMJHJBDZzhIaDlr-CX.2',
    '_chartbeat5': '',
    'amplitude_id_90784da74a890ce7c5669fa7473a7b6fnouvelobs.com': 'eyJkZXZpY2VJZCI6ImI5MDY1YjdmLTgwMzMtNDg2Zi1hMDJhLTU5MGU3ZTViYzM4YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3OTg0MjAwMjM5OCwibGFzdEV2ZW50VGltZSI6MTY3OTg0MjA2MjM1MCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjJ9',
    'obs_auth': '2524c6b39d28b4fe.be92XLxfhGvsyjVI8DOdy9uVsjzDAe9NCe5fXK5yquzsvhd%2FGpJpkPDbQooqmmcNr5moFqKQv05Rtx8JsPewKvXWweyWHwIOuyNEgOWwbq6ryOrFVE3GAycSPZGLbRRDBa7%2BCJ6rEGgvKz3GkyehtQive92bpzaBiv8ij2ZSsrJPD5VDOuS%2F3EhlnBoiNZIyuUCn%2F%2BLuwBOULQVVtsiELK4JiHfw1I9pEc6SU9pQOC2BSK4FidGoxrZ1ErrztcrMDkPmrxc7bnmPcNDOXnIbIP4fLIyeZlH6d0trEk1UBkjtq4bII3%2B2YKvE9W0yga%2FQ1k%2FF3OlerSj6DrqLVsLyKv8usIt%2FOriDi1sLtEZ5U%2Bt2MKy4DY59EnlnwHe7LNZWmiQFLfWOJpljwOXwZGwHEZbUqaqZqdZU1CTGJvM%2FNQ76bct5M%2Bu6IsOCVbXLORhWVzNGuldwlDq%2BONaXWYkkqdFCBxQD2vswYKvaKajLhbuHhsuQQCk5CWm6rWBD8RLEBy8tUJPrN%2FhbCG2NSFU5cpe6Q3TPnv31gE5DTlZzJvUXHjI8JWVOhPxyynvQVvENYkyzqB9surSzRYPUjkktkPnIrSc5Gxc4KtqqHCqovHl5TDOqFj%2BV1gft5ejjvuKg4EGYC%2FrhiDyOk4VxmhTKIj5%2BiMv2BPUo0VZ%2FpX5%2BZfqqOLK3QApU4pOJa1y9eWGjAQeUphd5b%2FuSOCj6TwxpKxvELtF7PurkIRZwXCpSvE5h0fAFj1gIppgqECIhVuo6pf%2BldaHjLk7PfnXBXOgNS8GN4eI%2FRA5iHzFgbg4uV36E4Y8KTwFvvI8Nfef2fTRy',
    'obs_sso_twipe': 'XxClOruJkUse7Z6MVKswTyrq1gZuCPJCp483QNkbV20D5ixm39%2FF%2FShRQCDO8vWF',
    'swg_trigger_linking': 'R6NjUEwLSVr0aUyY4KPm3Imr9-Ztfg0Q-MQIKNr4FrIv_FxCfd_nOfj7AC821L3QzT_k4LHm2Vp0E5dUfAjpiGqSSGfhjieIUF1nPPbtlCl2ZJLUHHoy-dSurMyX7RsP6pIxwPpkn6g8L4wGMy3dF5CqNkFHZSKfnh6aJZnRhWwQ1B84-nmOQN9VXhb7dhR7c7DjabyU2p07Pp-NIyKm3WUxpIFCV8NcX7YBrScrX5NBbgjHXS689IBnL9RnbhnokUBcwRqhH1zk6FY-DzNSDzDQ05tEQkaNK78viVyFcg0F1hs7rBvyNep5pdVib5GlrZ5uColfA9YaxJT_ovAkqt8tfFJ8py53IWzZqbk-2106I9E-9PxCDT9J73991wDcvL6k',
}

headers = {
    'authority': 'www.nouvelobs.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'G_AUTH2_MIGRATION=informational; critical-css-home=71277d09197ab98bd4ce753985a5c8d9; euconsent-v2=CPpIRAAPpIRAAFzABBFRC8CsAP_AAH_AAAqIJTNf_X__b3_v-_7___t0eY1f9_7__-0zjhfdt-8N3f_X_L8X_2M7vF36tr4KuR4ku3bBIUdtHPncTVmx6olVrzPsbk2cr7NKJ_Pkmnsbe2dYGH9_n9_z_ZKZ7___f__7_______________________________________________________________________-8EmwCTDVuIAuxLHAm2jCKBECMKwkKoFABRQDC0QGEDq4KdlcBPrCJAAgFAEYEQIcAUYMAgAAAgCQiICQI8EAgAIgEAAIAFQiEABGwCCgAsBAIABQDQsUYoAhAkIMiIiKUwICJEgoJ7KhBKD_Q0whDrLACg0f8VCAiUAIVgRCQsHIcESAl4skCzFG-QAjACgFEqFagk9NAAA; lmd_consent=%7B%22userId%22%3A%2277b3ced3-8768-49d6-956c-537e94efc623%22%2C%22timestamp%22%3A%221679673149.253987654%22%2C%22version%22%3A1%2C%22cmpId%22%3A371%2C%22displayMode%22%3A%22standard%22%2C%22purposes%22%3A%7B%22analytics%22%3Atrue%2C%22ads%22%3Atrue%2C%22personalization%22%3Atrue%2C%22mediaPlatforms%22%3Atrue%2C%22social%22%3Atrue%7D%7D; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22default%22%2C%22visitor_mode%22%3A%22optin%22%7D%2C%22options%22%3A%7B%22end%22%3A%222024-04-24T15%3A52%3A29.387Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _fbp=fb.1.1679673149496.873904607; _gcl_au=1.1.1482063594.1679673150; _cb=CDU-k-Cvm3NkCmnsKH; uid_dm=4ebaeb2d-631b-bfa8-7ece-83399c950a06; lead=2aadc901-aee7-4a24-b62a-8a71036b14df; __gads=ID=16e428f4526358ae-2208f935e4de00e6:T=1679673149:S=ALNI_MZ_9gCd-6YfH7c6PrV8xQjfqzUjWQ; obs_ab_v2=%7B%22paywall_length%22%3A%5B%22450%22%2C%22desktop%22%2C%22index%22%5D%7D; critical-css-article-v2=71277d09197ab98bd4ce753985a5c8d9; JSESSIONID=45a125b91ec12c37ef00e9414977; lobs_thruTunnel=true; _tt_enable_cookie=1; _ttp=vieyxujSHc1c9nVXqdYqAeoki_v; m_ses=20230324120101; m_cnt=3; sbt_i=5NzQzLWZhMGZjMGJhNmY1NTs7Njc3Y2M2ZjAtNDE2ZC00M2U4LTlmYmMtNzRlNmNiMmVhMTFhOzMDM3ZWY4OTgtYTE5NS00NWZiLWE0Y2EtZGIxM2QyMzBiNDgzOzM2M2M4MmM4LWYzYTAtNDg3ZC0A=; lmd_cap=_o1fsq189k; lobsNLPolitique=2023-3-24*2; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-561552-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; lobs_sc_cntr=Ma9qE9eFEP0ONTfPlGwZXkpIw08%3D; g_state={"i_p":1680379922776,"i_l":3}; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-561552-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; lobs_inscrits_1-counter=20230308.OBS70477%2C20230324.OBS71311%2C20230324.OBS71326%2C20230322.OBS71232%2C20221107.OBS65629%2C20221106.OBS65566%2C20230323.OBS71272%2C20230314.OBS70789%2C20230315.OBS70894%2C20230309.OBS70581%2C20230321.OBS71185%2C20230321.OBS71176%2C20230322.OBS71186%2C20230325.OBS71360%2C20230325.OBS71345%2C20230206.OBS69226; lastAboTeaser=20230324.OBS71311_Retraites_Et_Si_Emmanuel_Macron_S_Offrait_Une_Porte_De_Sortie_Avec_L_Article_10_De_La_Constitution; lobs_inscrits_1=Qp8d8wzB0GiGINauXRdnK7lKRm0%2B8OiS; _cb_svref=null; __gpi=UID=00000a2faa8c98d6:T=1679673149:RT=1679842002:S=ALNI_Ma4tBJfmtxoMg0glxcQx1UpF0ACQQ; cto_bundle=RiYcjF9hYklxY2lzQWdvSUc2WSUyRjQycUNrYlVHNXR1Z2VCa1BhVmpZOVg4YlladjJoZjhNRndZdiUyQnp1TGRKMk1oWFBSTGMwNSUyRnBQd1VIU3BQVHpPZHltT0lta0ZMM1QxTUFhMmx2cWtNek1uT1J1dnFrbmNaVFc4SXpvNEJjc1dBcEJCQ1NXa0tJSWk2eFlBU1UlMkJnd2ltWiUyQjNJQkI1bURFQVBmbE9NdGFETDNUOTRoR1N5Q0NFYmZqOEs1blQ0TWNYR1NqUUUlMkZieTdBVWclMkJtSVZKWkoxV0tzOEElM0QlM0Q; _chartbeat2=.1675788051481.1679842062322.0000000000000111.maabfBemdtYBMJHJBDZzhIaDlr-CX.2; _chartbeat5=; amplitude_id_90784da74a890ce7c5669fa7473a7b6fnouvelobs.com=eyJkZXZpY2VJZCI6ImI5MDY1YjdmLTgwMzMtNDg2Zi1hMDJhLTU5MGU3ZTViYzM4YlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3OTg0MjAwMjM5OCwibGFzdEV2ZW50VGltZSI6MTY3OTg0MjA2MjM1MCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjJ9; obs_auth=2524c6b39d28b4fe.be92XLxfhGvsyjVI8DOdy9uVsjzDAe9NCe5fXK5yquzsvhd%2FGpJpkPDbQooqmmcNr5moFqKQv05Rtx8JsPewKvXWweyWHwIOuyNEgOWwbq6ryOrFVE3GAycSPZGLbRRDBa7%2BCJ6rEGgvKz3GkyehtQive92bpzaBiv8ij2ZSsrJPD5VDOuS%2F3EhlnBoiNZIyuUCn%2F%2BLuwBOULQVVtsiELK4JiHfw1I9pEc6SU9pQOC2BSK4FidGoxrZ1ErrztcrMDkPmrxc7bnmPcNDOXnIbIP4fLIyeZlH6d0trEk1UBkjtq4bII3%2B2YKvE9W0yga%2FQ1k%2FF3OlerSj6DrqLVsLyKv8usIt%2FOriDi1sLtEZ5U%2Bt2MKy4DY59EnlnwHe7LNZWmiQFLfWOJpljwOXwZGwHEZbUqaqZqdZU1CTGJvM%2FNQ76bct5M%2Bu6IsOCVbXLORhWVzNGuldwlDq%2BONaXWYkkqdFCBxQD2vswYKvaKajLhbuHhsuQQCk5CWm6rWBD8RLEBy8tUJPrN%2FhbCG2NSFU5cpe6Q3TPnv31gE5DTlZzJvUXHjI8JWVOhPxyynvQVvENYkyzqB9surSzRYPUjkktkPnIrSc5Gxc4KtqqHCqovHl5TDOqFj%2BV1gft5ejjvuKg4EGYC%2FrhiDyOk4VxmhTKIj5%2BiMv2BPUo0VZ%2FpX5%2BZfqqOLK3QApU4pOJa1y9eWGjAQeUphd5b%2FuSOCj6TwxpKxvELtF7PurkIRZwXCpSvE5h0fAFj1gIppgqECIhVuo6pf%2BldaHjLk7PfnXBXOgNS8GN4eI%2FRA5iHzFgbg4uV36E4Y8KTwFvvI8Nfef2fTRy; obs_sso_twipe=XxClOruJkUse7Z6MVKswTyrq1gZuCPJCp483QNkbV20D5ixm39%2FF%2FShRQCDO8vWF; swg_trigger_linking=R6NjUEwLSVr0aUyY4KPm3Imr9-Ztfg0Q-MQIKNr4FrIv_FxCfd_nOfj7AC821L3QzT_k4LHm2Vp0E5dUfAjpiGqSSGfhjieIUF1nPPbtlCl2ZJLUHHoy-dSurMyX7RsP6pIxwPpkn6g8L4wGMy3dF5CqNkFHZSKfnh6aJZnRhWwQ1B84-nmOQN9VXhb7dhR7c7DjabyU2p07Pp-NIyKm3WUxpIFCV8NcX7YBrScrX5NBbgjHXS689IBnL9RnbhnokUBcwRqhH1zk6FY-DzNSDzDQ05tEQkaNK78viVyFcg0F1hs7rBvyNep5pdVib5GlrZ5uColfA9YaxJT_ovAkqt8tfFJ8py53IWzZqbk-2106I9E-9PxCDT9J73991wDcvL6k',
    'referer': 'https://www.nouvelobs.com/connexion',
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

#response = requests.get('https://www.nouvelobs.com/', cookies=cookies, headers=headers)


MASTER_URL = 'https://www.nouvelobs.com'
def test_main():
     tables = []
     response = requests.get('https://www.nouvelobs.com/', cookies=cookies, headers=headers)
     print(response)
     crawl_link_page('https://www.nouvelobs.com/culture', tables)
     for i in range(2, 40): #based on liberation website structure
        new_link = MASTER_URL + '/culture/page/' + str(i) 
        print(new_link)
        try:
            crawl_link_page(new_link, tables)
        except Exception as ex: 
            if ex.code == 404:
                break
        print(i)
     df = pd.DataFrame(data=tables)
     df.to_csv('obs_culture.csv',encoding='utf-8')

def crawl_link_page(url, tables):
    # single page chosen from news website
    response = requests.get(url, cookies=cookies, headers=headers)
    print(response.url)
    html_doc = response.text

    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    # all text of the article is in p tags
    #print(soup.find_all("article", {"class": "article-box"}))
    for article in soup.find_all("article", {"class": "article-box"}):
        link = article.a.get('href')
        #print(link)
        crawl_article(link, tables)
     
def crawl_article(link, tables):
    response = requests.get(link, cookies=cookies, headers=headers)
    print(response.url)
    html = response.text

    page_soup = bs4.BeautifulSoup(html, 'html.parser')
    try:
        date_x = page_soup.find(class_="article-page__published")
        date = date_x.time.get_text()
    except Exception as ex:
        date = ''
    
    
    
    paragraphs = page_soup.find_all('p') # class_='CustomContentListItem__Link-sc-2hcki7-2 kPzBgo'
    title = page_soup.find('h1')
    page = ""
    for paragraph in paragraphs:
        page += paragraph.get_text()
        #print(paragraph.get_text())
    row = [date, title, page]

    tables.append(row)



test_main()
