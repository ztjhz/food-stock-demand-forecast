# importing libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
import matplotlib.pyplot as plt
import datetime


def main():
    df = load_data_set()
    process_data(df)

def read_data_set(file_name):
    df = pd.read_csv(file_name)
    return df

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
        temp_df["Date"] = pd.to_datetime(temp_df["Date"]) # change date to datetime format
        temp_df = temp_df.sort_values(by="Date") # sort by date
        temp_df = temp_df.groupby(temp_df["Date"]).count()
        print(temp_df)
        forecast(temp_df, item)

def plot(temp_df):
    plt.figure(figsize=(16,8))
    plt.clf()
    plt.plot(temp_df['itemDescription'])
    plt.show()


def forecast(my_data, food_label):
    from statsmodels.tsa.arima.model import ARIMA

    # ARIMA MODEL after considering
    # p (order of autoregressive model)
    # d (degree of differencing)
    # q (order of moving-average model)
    model = ARIMA(my_data, order=(7, 0, 7))
    results_ARIMA = model.fit()

    # plt.plot(my_data)
    # plt.plot(results_ARIMA.fittedvalues, color='red')
    # plt.show()
        
    # predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
    # print(predictions_ARIMA_diff.tail())

    # forecast results
    x = results_ARIMA.forecast(steps=30)
    x.index = np.arange(1, len(x.index) + 1)
    print(x)

    # plot graph
    plt.plot(x)
    plt.title(food_label)
    plt.xlabel("Days Into The Future")
    plt.ylabel("Food Demand")
    # plt.show()
    plt.savefig("Forecast/{}".format(food_label.replace("/", ",")))
    plt.clf()
    plt.cla()
    plt.close()
    return x
    

main()