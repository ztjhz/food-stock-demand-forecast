# Food Stock Demand Forecast

Dataset: https://www.kaggle.com/heeraldedhia/groceries-dataset

## The Issue
Food waste is a common problem in Singapore for retail outlets (e.g. supermarkets) due to the perishable nature of food. Since they do not know how much food demand to expect in the future, they would stock up excess food as they would not want to disappoint customers due to lack of stock. Thus the excess perishable stock would be wasted, leading to the serious food waste problem in Singapore.

## Why we want to tackle this issue
264.2 million people (20%) in sub-Saharan Africa were undernourished and experiencing hunger in 2020. By channeling the surplus of food to other nations who are facing food supply shortages, we reduce the problem of global food wastage. It is a basic human right to have proper access to nutritious food. Hence, we hope that through our idea, we can help divert the food that was supposed to be wasted to people in Africa.

## Solution
To tackle this issue, our team came up with this idea of Time Series Forecasting which implements Machine Learning to predict future food demand. Users can input their past sales record over a period of time, and see how much demand for food they can expect.

### Time Series Forecasting
### Steps Took:
1. Load groceries dataset into a pandas dataframe
2. Clean the data and process the data into useable dataframe
3. Use ARIMA to build a model to forecast future food demand
4. Plot future food demand in a graph and save it as a png

### How can this be implemented in the real world:
#### Mobile Application:
- Users can store past sales data over a period of time
- A forecast function that uses the above algorithm implemented
