import pandas as pd
import time
import random
from datetime import datetime

def get_data(url,liga):
    tiempo = [1,3,2]
    time.sleep(random.choice(tiempo))
    df = pd.read_html(url)
    df = pd.concat([df[0],df[1]], ignore_index=True,axis=1)
    df = df.rename(columns={0:'EQUIPO', 1:'J', 2:'G',3:'E', 4:'P', 5:'GF',6:'GC',7:'DIF',8:'PTS'})
    df['EQUIPO'] = df['EQUIPO'].apply(lambda x: x[5:] if x[:2].isnumeric() ==True else x[4:])
    df['LIGA'] = liga

    run_date = datetime.now()
    run_date = run_date.strftime("%Y-%m-%d")
    df['CREATE_AT'] = run_date

    return df


#ligas = ['COLOMBIA','INGLATERRA','ESPAÑA','ALEMANIA','FRANCIA','ITALIA']

def data_processing(df):
    df_colombia = get_data(df['URL'][0],df['LIGA'][0])
    df_inglaterra = get_data(df['URL'][1],df['LIGA'][1])
    df_españa = get_data(df['URL'][2],df['LIGA'][2])
    df_alemania = get_data(df['URL'][3],df['LIGA'][3])
    df_francia = get_data(df['URL'][4],df['LIGA'][4])
    df_italia = get_data(df['URL'][5],df['LIGA'][5])

    df_final = pd.concat([df_colombia,df_inglaterra,df_españa,df_alemania,df_francia,df_italia], ignore_index=True)

    return df_final