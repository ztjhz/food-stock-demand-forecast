# importing libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
from bs4 import BeautifulSoup
import requests # library to handle requests
import json # library to handle JSON files
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
import datetime


def main():
    df = read_data_set("Groceries_dataset.csv")
    process_data(df)

def process_data(df):
    # sort df by date and drop unused columns
    # df = df.sort_values(by="Date")
    df = df.drop(columns=['Member_number'], axis=1)
    
    # start_date = df["Date"].iloc[0]
    # print(start_date)
    valid_df = df.groupby(by="itemDescription").count().sort_values(by="Date")
    valid_df = valid_df.drop(valid_df[valid_df.Date < 1000].index)
    print(valid_df.count())
    

def read_data_set(file_name):
    df = pd.read_csv(file_name)
    return df

main()