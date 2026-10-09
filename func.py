from datetime import date, timedelta
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests
import random
import time
import os


date_value = 0

def main_date(day):
    last_date = date.today() + timedelta(day)
    return last_date



def save_daily_csv():
    outcome_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'CSV FILES')
    todays_dir = str(main_date(date_value))+' Files'
    full_path = os.path.join(outcome_dir,todays_dir)
    try:
        os.makedirs(full_path)
    except:
        print('\n PATH ALREADY EXIST BUT WAS CREATED SUCCESFULLY \n')
    return full_path
    


def drop_date(path):
    df = pd.read_csv(path)
    current_date = str(main_date(date_value)).split('-')[-1]
    if current_date.startswith('0'):
        current_date = current_date.replace('0','')
    print(current_date)

    df = df[df['DATE'].astype(str).str.startswith(current_date)].reset_index(drop='index')
    df.to_csv(path, index=False)





def saving_files(data,path):
    df = pd.DataFrame(data)
    print(df.to_string())

    try:
        df2 = pd.read_csv(path)
        all_df = pd.concat([df2, df], ignore_index=True)
        all_df.to_csv(path, index=False)
        print(' ------------------------------------ ALL FILES SAVED  ------------------------------------- \n \n')

    except:
        df.to_csv(path, index=False)
        print('============================= SECOND FILE SAVED ==========================')



def drop_duplicate(path):
    all_df = pd.read_csv(path)
    all_df = all_df.drop_duplicates(keep='first')
    all_df = all_df.reset_index()
    all_df.drop(['index'], axis=1, inplace=True)
    all_df.to_csv(path, index=False)


def sorting_values(path,path_to,value):
    df = pd.read_csv(path)
    df = df.sort_values(by=value,ascending=False)
    df.to_csv(path_to, index=False)



def daily_pred(path,path_to,**kwargs):
    data = {'DATE':[],'TIME':[],'LEAGUE':[],'HOME TEAM':[],'AWAY TEAM':[],'TIP CATE':[],'TIP':[],'TIP PER':[],'SUP CATE':[],'SUP TIP':[],'SUP PER':[]}

    df = pd.read_csv(path)
    kwarg_keys = [x.replace('_1','1') for x in kwargs.keys()]
    kwarg_values = list(kwargs.values())

    sort1 = list(df[kwarg_values[0]]).count(max(df[kwarg_values[0]]))
    if sort1 > 1:
        df = df.iloc[:sort1,:]
        df = df.sort_values(by=f'{kwarg_values[1]}',ascending=False).reset_index()

        data['DATE'].append(df['DATE'][0])
        data['TIME'].append(df['TIME'][0])
        data['LEAGUE'].append(df['LEAGUE'][0])
        data['HOME TEAM'].append(df['HOME TEAM'][0])
        data['AWAY TEAM'].append(df['AWAY TEAM'][0])
        data['TIP CATE'].append(kwarg_keys[0])
        data['TIP'].append(df[kwarg_keys[0]][0])
        data['TIP PER'].append(df[kwarg_values[0]][0])

        data['SUP CATE'].append(kwarg_keys[1])
        data['SUP TIP'].append(df[kwarg_keys[1]][0])
        data['SUP PER'].append(df[kwarg_values[1]][0])
        saving_files(data=data,path=path_to)


    else:
        data['DATE'].append(df['DATE'][0])
        data['TIME'].append(df['TIME'][0])
        data['LEAGUE'].append(df['LEAGUE'][0])
        data['HOME TEAM'].append(df['HOME TEAM'][0])
        data['AWAY TEAM'].append(df['AWAY TEAM'][0])
        data['TIP CATE'].append(kwarg_keys[0])
        data['TIP'].append(df[kwarg_keys[0]][0])
        data['TIP PER'].append(df[kwarg_values[0]][0])

        data['SUP CATE'].append(kwarg_keys[1])
        data['SUP TIP'].append(df[kwarg_keys[1]][0])
        data['SUP PER'].append(df[kwarg_values[1]][0])
        saving_files(data=data,path=path_to)




