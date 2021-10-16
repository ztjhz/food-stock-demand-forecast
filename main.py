# importing libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
from bs4 import BeautifulSoup
import requests # library to handle requests
import json # library to handle JSON files
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe


def main():
    df = read_data_set("Groceries_dataset.csv")
    process_data(df)

def process_data(df):
    df = df.sort_values(by="Date")
    print(df)

def read_data_set(file_name):
    df = pd.read_csv(file_name)
    return df

main()