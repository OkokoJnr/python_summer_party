import pandas as pd

# Define the data
dim_product = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'product_name': [
        'Smart TV', 'Wireless Earbuds', 'Refrigerator', 'Bestselling Novel',
        'Designer Jeans', 'Blender', 'Tent', 'Smart Home Hub',
        'Phone Charger', 'Skincare Set', 'Drone', 'Car Charger'
    ],
    'product_category': [
        'Home Electronics', 'Electronics & Gadgets', 'Electronics Appliances', 'Books',
        'Fashion', 'Kitchen', 'Outdoor', 'Home Electronics',
        'Electronics Accessories', 'Health & Beauty', 'Electronics Gadgets', 'Automotive'
    ]
})

fct_ad_performance  = pd.DataFrame({
    
    'ad_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'clicks': [10, 15, 20, 18, 5, 12, 50, 8, 14, 22, 30, 7, 13, 9, 16],
    'product_id': [1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 9, 11, 11, 12, 2],
    'impressions': [200, 300, 250, 230, 150, 180, 500, 250, 200, 220, 300, 120, 150, 190, 160],
    'recorded_date': [
        '2024-10-02', '2024-10-12', '2024-10-05', '2024-10-20',
        '2024-10-15', '2024-10-25', '2024-10-07', '2024-10-18',
        '2024-10-10', '2024-10-30', '2024-10-08', '2024-10-22',
        '2024-10-28', '2024-10-11', '2024-11-01'
    ]
})

# Convert recorded_date to datetime
fct_ad_performance['recorded_date'] = pd.to_datetime(fct_ad_performance['recorded_date'])

# TASK 1: What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring 'Electronics' in its name during October 2024? This analysis will help determine which electronics-related categories are performing optimally.
#
oct_2024_ads = fct_ad_performance[(fct_ad_performance['recorded_date'].dt.year == 2024) & (fct_ad_performance['recorded_date'].dt.month == 10)]
electronics_prdt = dim_product[dim_product['product_category'].str.contains('Electronics')]
# Merge the two DataFrames on product_id
electronics_prdt_oct_2024_ads = pd.merge(oct_2024_ads, electronics_prdt, on = 'product_id')
# Calculate the click-through rate (CTR)
electronics_prdt_oct_2024_ads['ctr'] = (electronics_prdt_oct_2024_ads['clicks'] / electronics_prdt_oct_2024_ads['impressions']) * 100
# Group by product category and calculate the average CTR
electronics_prdt_oct_2024_ads_avg = electronics_prdt_oct_2024_ads.groupby('product_category')['ctr'].mean().reset_index()   



print(electronics_prdt_oct_2024_ads_avg)