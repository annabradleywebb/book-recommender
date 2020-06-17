from pynytimes import NYTAPI
import pandas as pd
import time
import datetime
import pickle

def make_book_dict(list_of_dates):
    master_df = pd.DataFrame()
    for i in range(len(list_of_dates)):
        df = pd.DataFrame(nyt.best_sellers_list(date = datetime.datetime(list_of_dates[i][0],list_of_dates[i][1],list_of_dates[i][2])))
        date_test = list_of_dates[i]
        df['date'] = str(date_test)
        master_df = master_df.append(df)
        print(i)
        time.sleep(6)
    return master_df

