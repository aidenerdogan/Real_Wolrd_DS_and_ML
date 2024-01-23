#import libraries for data analysis (pandas) and argument parsing
import pandas as pd
import sys
import argparse

#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--min-date",  required=True)
parser.add_argument("--max-date",  required=True)
parser.add_argument("--top", required=True, type=int )


#comman line arguments
min_date=sys.argv[2] 
max_date=sys.argv[4]  
top_values=int(sys.argv[6])


product_data = pd.read_csv('product.csv')
sales_data = pd.read_csv('sales.csv')
store_data = pd.read_csv('store.csv')

#rename 'id' columns
store_data.rename(columns={'id':'store_id'},inplace=True)
product_data.rename(columns={'id':'product_id'},inplace=True)

main_data = sales_data.merge(store_data,how="inner", left_on='store', right_on='store_id'
).merge(product_data, how="inner",left_on='product', right_on='product_id'
).drop(columns=['store_id', 'product_id']).rename(columns={'name_x':'store_name','name_y':'product_name'})


#Datas between min and max dates in pandas  
framed_data = main_data.loc[(main_data['date'] > min_date) & (main_data['date'] <= max_date)]

"--------------------Top Seller n Products--------------------"
#get product_name and quantitity in given date range   
data_product=framed_data[["product_name", "quantity"]]
#get sum of quantity via grouping products
data_product=data_product.groupby(['product_name']).sum()
#sort values by descending 
data_product=data_product.sort_values(by='quantity', ascending=False)
print("\n\n-- top seller product --")
print(data_product.head(top_values)) 

"--------------------Top Seller n Stores--------------------"
#store_name and quantity in given date range 
data_store=framed_data[["store_name", "quantity"]]
#get sum of quantity via grouping stores
data_store=data_store.groupby(['store_name']).sum()
#sort values by descending 
data_store=data_store.sort_values(by='quantity', ascending=False) 
print("\n\n-- top seller store --")
print(data_store.head(top_values)) 

"--------------------Top Seller n Brands--------------------"
#brand and quantity in given date range
data_brand=framed_data[["brand", "quantity"]]
#get sum of quantity via grouping brands
data_brand=data_brand.groupby(['brand']).sum()
#sort values by descending 
data_brand=data_brand.sort_values(by='quantity', ascending=False)
print("\n\n-- top seller brand --")
print(data_brand.head(top_values)) 

"--------------------Top Seller n Cities--------------------"
#city and quantity in given date range   
data_city=framed_data[["city", "quantity"]]
#get sum of quantity via grouping cities
data_city=data_city.groupby(['city']).sum() 
#sort values by descending 
data_city=data_city.sort_values(by='quantity', ascending=False)
print("\n\n-- top seller city --")
print(data_city.head(top_values))
