# importing libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
from bs4 import BeautifulSoup
import requests # library to handle requests
import json # library to handle JSON files
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
import datetime


def main():
    df = load_data_set()
    process_data(df)

def load_data_set():
    df = read_data_set("Groceries_dataset.csv")
    for i in range(5):
        df2 = read_data_set("Groceries_dataset.csv")
        df = df.append(df2)
    return df

def process_data(df):
    # sort df by date and drop unused columns
    # df = df.sort_values(by="Date")
    df = df.drop(columns=['Member_number'], axis=1)
    
   
    # get items with many data points
    valid_items_df = df.groupby(by="itemDescription").count().sort_values(by="Date")
    valid_items_df = valid_items_df.drop(valid_items_df[valid_items_df.Date < 5000].index)
    
    for item in valid_items_df.index:
        temp_df = df[df.itemDescription == item]
        # temp_df = temp_df.sort_values(by="Date")
        temp_df["Date"] = pd.to_datetime(temp_df["Date"])
        temp_df = temp_df.sort_values(by="Date")
        # temp_df = pd.to_datetime(temp_df["Date"])
        print(temp_df.tail())
        print()

def read_data_set(file_name):
    df = pd.read_csv(file_name)
    return df

main()