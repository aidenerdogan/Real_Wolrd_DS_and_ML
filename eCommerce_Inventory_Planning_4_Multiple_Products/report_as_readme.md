# The Report for Data Challenge

### **Challenge Description: eCommerce Inventory Planning for Multiple Products**

Build a time series forecasting model that helps eCommerce merchants plan their monthly inventory purchasing for the year 2023 for multiple products on M5-Accuracy Compatation data.
## Dataset Description

The M5 dataset, generously made available by Walmart, involves the unit sales of various products sold in the USA, organized in the form of grouped time series. More specifically, the dataset involves the unit sales of 3,049 products, classified in 3 product categories (Hobbies, Foods, and Household) and 7 product departments, in which the above-mentioned categories are disaggregated.  The products are sold across ten stores, located in three States (CA, TX, and WI). In this respect, the bottom-level of the hierarchy, i.e., product-store unit sales can be mapped across either product categories or geographical regions, as follows:

![](images/dataset_diagram.png)

image source: kaggle

## Insights from EDA

### 20 different items

![](images/eda1.PNG)

### Sales by store category

![](images/eda2.PNG)


![](images/eda3.PNG)




## Feature Selection and Engineering
- Data Features
- Lag Features
- Creating new fetures
- Standard Scalar to normalize the features

## Data Preprocessing
- Merged and melted data frames
- Removed unnecessary columns
- Cleaned from noises
- Created new columns
- Splitting data into training and testing datasets
- Normalized the features with Standard Scalar


## Model Selection
I use the RMSE and norm_error loss evaluation metric for each model to select the highest performing model.  The model with the lowest RMSE has the best fit to the data for forecasting the m5 sales data.  The models I use were Holt-Linear (exponantial smoothing),Holt-Winter (Double Exponantial Smooothing),ARIMA (Mooving Avarage), SARIMAX, LGBM Regressor. The best performing model is LGBM Regressor with approximately 2.3 (even for 120 itarations) RMSE.  This is the model I will use for the forecasting of m5 sales data for 28 days (a month by 4 weeks which is important while forecasting data has weekly seasonality).


*** Also in lgbm modelling notebook (model&data_pipeline.ipynb) I created data pipeline from sunmission data which can be anytime new came data. ***
## Relative Important Features

![](images/lgbm_importances-01.PNG)

The light GBM model performed fairly well with an RMSE over the folds is approximately 2.3. I can see from the relative feature importance that the top 3 features were item_id, store_id, sell_price, and week. I think item_id and sell_price makes sense to be the top features for the forecast because the forecast will depend on the items and price of the items. Week also makes sense because the forecast depends on time parameters to make a forecast, so having a time parameter in the top three relative important features is logical.

## Further Investigation
- More Feture Engineering for prophet and sarimax models.
- Developing a Neural Network model with LSTM and comparing lastyly tuned Prophet, tuned SRIMAX, LSTM and LGBM.
- Creating dynamic data pipline with last selected model on cloud or onprem with APIs (FastAPI or Flask API)

# Notebook File Explanations

### File single shot:

- Understanding data
- Defineing and handling trends, seasonality
- single product forecasting with sarimax and prophet

### File eda-ml and stats:

- well explained EDA on data
- handling missing values and feture enginering
- handling trendding, seasonality and noises
- creating stat and ml forecasting models for multiple products
- comparing models on norm-error-loss

### File model and data pipeline:

- developing lgbm model for best practice
- saving model
- creating data pipeline
- connecting data pipeline with model to predict new datas
- feature selecting  
Sources:

In This work I got help from Kaggle, stackoverflow and chatGPT (detailed method explanations)
