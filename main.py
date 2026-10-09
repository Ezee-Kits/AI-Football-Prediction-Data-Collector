from func import main_date,saving_files,drop_duplicate,save_daily_csv,sorting_values,daily_pred,drop_date
from datetime import date, timedelta
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests
import time
import func
import os 




full_path = save_daily_csv()

m_date = func.date_value
path = f'{full_path}/{main_date(m_date)} Rating_File.csv'

_1x2_path = f'{full_path}/{main_date(m_date)} 1x2_File.csv'
over_under_path = f'{full_path}/{main_date(m_date)} over_und_File.csv'
bts_path = f'{full_path}/{main_date(m_date)} bts_File.csv'
dc_path = f'{full_path}/{main_date(m_date)} dc_File.csv'
ht_ft_path = f'{full_path}/{main_date(m_date)} ht_ft_File.csv'

stake_path = f'{full_path}/{main_date(m_date)} Stake_File.csv'


td_url = 'https://www.accagenerator.com/football-predictions/'
tmr_url = 'https://www.accagenerator.com/football-predictions/tomorrow/'


res = requests.get(td_url)
soup = BeautifulSoup(res.content,"html.parser")

links = [name.get('href') for name in soup.findAll('a')]
# print(links)


all_links =[]
for link in links:
    if link.startswith('https://www.accagenerator.com/football-tips-and-predictions-for') and link not in all_links:
        all_links.append(link)
# print(all_links)
#all_links = all_links[66:]
print('LENGHT OF ALL LINKS = ',len(all_links))



ex_link = ['1x2-predictions/','over-under-predictions','both-teams-score-predictions/','double-chance-predictions/','ht-ft-predictions/']#,'corners-predictions/'

for i,x in enumerate(all_links):
    print(x)
    data = {'DATE': [],
        'TIME': [],
        'LEAGUE': [],

        'HOME TEAM': [],
        'AWAY TEAM': [],

        '1X2': [],
        '1X2 PER':[],

        'OVER_UNDER': [],
        'OVER_UNDER PER':[],

        'BTS_OTS':[],
        'BTS_OTS PER':[],

        'Double_Chance':[],
        'Double_Chance PER':[],

        'HT_FT':[],
        'HT_FT PER':[]

        }
    
    for xlink in ex_link:
        res = requests.get(x+xlink)
        soup = BeautifulSoup(res.content,"html.parser")
        tree = html.fromstring(res.content)

        index_pos = i
        print(f'>>>>>>>>>>>>>>>>>>>>  NUMBER = {index_pos+1} HAS STARTED TO RUN, WITH TOTAL RUNS OF {len(all_links)}  & REMANING OF {len(all_links) - (index_pos+1)} <<<<<<<<<<<<<<<<<<<< \n')

        
        tip_info = soup.select('#accagen-banner > div > div > div.accagen-banner-text.accagen-headline > h1')[0].text
        try:
            for all_pred in range(0,20):
                each_row = soup.select('#accagen-banner > div > div > div:nth-child(3) > ul > li:nth-child('+str((2*all_pred) + 1)+')')[0]

                pred_date = each_row.find('div',class_="datecombos").text.split()

                league = each_row.find('span',class_="tips-card__league").text.split('\n')[-1]
                teams = each_row.find('h3',class_="tips-card__name-first").text.split('vs')
                
                tip = each_row.find('div',class_="tipdetail").text
                tip_per = int(each_row.find('span',class_="count-text").get('data-stop'))
                print(pred_date, league,teams,tip, tip_per)

                if '1x2' in tip_info:
                    data['DATE'].append(pred_date[1])
                    data['TIME'].append(pred_date[3])
                    data['LEAGUE'].append(league)
                    data['HOME TEAM'].append(teams[0])
                    data['AWAY TEAM'].append(teams[1])
                    data['1X2'].append(tip)
                    data['1X2 PER'].append(tip_per)


                if 'BTTS' in tip_info:
                    data['BTS_OTS'].append(tip)
                    data['BTS_OTS PER'].append(tip_per)

                if 'Over Under' in tip_info:
                    data['OVER_UNDER'].append(tip)
                    data['OVER_UNDER PER'].append(tip_per)

                if 'HT/FT' in tip_info:
                    data['HT_FT'].append(tip)
                    data['HT_FT PER'].append(tip_per)

                if 'Double Chance' in tip_info:
                    data['Double_Chance'].append(tip)
                    data['Double_Chance PER'].append(tip_per)

        except:
            print('\n \t ERROR OCCURED WHEN SCRAPING \n ')
    saving_files(data=data,path=path)
    

drop_duplicate(path=path)
drop_date(path=path)


sorting_values(path=path,path_to=_1x2_path,value='1X2 PER')
sorting_values(path=path,path_to=over_under_path,value='OVER_UNDER PER')
sorting_values(path=path,path_to=bts_path,value='BTS_OTS PER')
sorting_values(path=path,path_to=dc_path,value='Double_Chance PER')
sorting_values(path=path,path_to=ht_ft_path,value='HT_FT PER')



# daily_pred(path=_1x2_path,path_to=stake_path,_1X2 ='1X2 PER',HT_FT ='HT_FT PER')
# daily_pred(path=ht_ft_path,path_to=stake_path,HT_FT ='HT_FT PER',_1X2 ='1X2 PER')

# daily_pred(path=over_under_path,path_to=stake_path,OVER_UNDER = 'OVER_UNDER PER',BTS_OTS ='BTS_OTS PER')
# daily_pred(path=bts_path,path_to=stake_path,BTS_OTS ='BTS_OTS PER',OVER_UNDER = 'OVER_UNDER PER')

# daily_pred(path=dc_path,path_to=stake_path,Double_Chance='Double_Chance PER',_1X2 ='1X2 PER')

