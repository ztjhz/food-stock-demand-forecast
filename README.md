# Food Stock Demand Forecast

Demo Website: https://ztjhz.github.io/food-stock-demand-forecast/

Demo Video: https://youtu.be/U9Tkbx5ir4M

Pitch Video: https://youtu.be/Smc3SEaGmCI

Pitch Deck: https://github.com/ztjhz/food-stock-demand-forecast/blob/main/Dino%20Bots%20Slide%20Deck.pdf

Dataset: https://www.kaggle.com/heeraldedhia/groceries-dataset

## The Issue

Food waste is a common problem in Singapore for retail outlets (e.g. supermarkets) due to the perishable nature of food. Amount of food waste generated has grown by around 20% over the last 10 years. In 2019, Singapore generated around 744 million kg of food waste. Since they do not know how much food demand to expect in the future, they would stock up excess food as they would not want to disappoint customers due to lack of stock. Hence, the excess perishable stock would be wasted, contributing to the worsening food waste problem in Singapore.

## Why we want to tackle this issue

1. Increasing amount of food waste puts pressure on our resources. We will need to build more waste disposal facilities, such as waste-to-energy plants and landfills for incineration ash. This is not sustainable for land-scarce Singapore. When food is wasted, so are all of the resources used to grow and deliver the food to our tables, as well as to dispose of it. This increases our carbon footprint, contributing to global warming and climate change.
2. Some 4.1 per cent of Singaporeans faced moderate to severe food insecurity between 2016 and 2018, according to the State of Food Security and Nutrition in the World 2019 report by the United Nations. A study conducted by the Lien Centre for Social Innovation at the Singapore Management University (SMU) surveyed 236 Singaporeans in four low-income neighbourhoods being served by food support groups. It found that nearly 1 in 5 participants in these areas reported severe food insecurity in 2018.

## Solution

To tackle these issues, we will be segmenting the solution into 2 parts:

1. Our team wants to make use of Time Series Forecasting which implements Machine Learning to predict future food demand. Users can input their past sales record over a period of time, and see how much demand for food they can expect and determine how much food to be purchased, minimising potential food wastage.
2. Beyond the lowest demand before its expiry date, these products could be donated to families who are in need

### Time Series Forecasting

### Steps Took:

1. Load groceries dataset into a pandas dataframe
2. Clean the data and process the data into useable dataframe
3. Use ARIMA to build a model to forecast future food demand
4. Plot future food demand in a graph and save it as a png

### How can this be implemented in the real world:

#### Web Application:

- Users can record and store past sales data over a period of time in an Excel/CSV file
- A forecast function that uses the above algorithm implemented can be used to forecast the future demand for food
- Utilising this knowledge, the next batch of food supplied to the user can be adjusted hence minimising the probability of excess food purchases
- Together with that concept, we can determine a threshold before the expiry date so that users can take these food and deliver them to families in need

## References

- https://www.towardszerowaste.gov.sg/foodwaste/
- https://www.channelnewsasia.com/cnainsider/food-insecurity-singapore-hunger-poverty-777806
