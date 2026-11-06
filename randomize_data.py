import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

conn = sqlite3.connect ('supply_chain.db')
cursor = conn.cursor()

#1 Create and fill out Vendors Table
# Define your vendors with IDs and locations
vendors_df = pd.DataFrame({
    'vendor_id': [1, 2, 3, 4, 5],
    'vendor_name': ["John's Products", "Tim's Inc", "Bob's B-21's", "Adam's Collection", "Sam's Storage"],
    'location': ['Chicago, IL', 'St. Louis, MO', 'Indianapolis, IN', 'Milwaukee, WI', 'Detroit, MI']
})

# 2. Generate some mock data using lists and loops 
# (e.g., create a list of 5-10 fake vendor names, and loop 100 times to generate random dates and costs)
vendors = [
    "John's Products",
    "Tim's Inc",
    "Bob's Burgers",
    "Adam's Collection",
    "Sam's Storage"
]

#Establishing Order Date
order_date = [datetime(2026,1,1) + timedelta(days=random.randint(0,30)) for _ in range(100)]
estimated_date = [d + timedelta(days=random.randint(7,14)) for d in order_date]
actual_date = [d + timedelta(days=random.randint(7,21)) for d in order_date]
order_status = ['Delayed' if act > est else 'On Time' for est, act in zip(estimated_date, actual_date)]

#Inputting lists above and SQL columns inside DataFrame (pd.DataFrame)
orders_df = pd.DataFrame({
'vendor_id': random.choices([1,2,3,4,5], k = 100),
'order_id': list(range(1,101)),
'units_ordered': [random.randint(10,500) for _ in range(100)],
'shipping_cost': [round(random.uniform(25,600), 2) for _ in range(100)],
'order_date' : order_date,
'estimated_date': estimated_date,
'actual_date' : actual_date,
#Determine order status
'order_status': order_status}) 

# 3. Use pandas to push it straight into SQLite!
orders_df.to_sql('orders', conn, if_exists='replace', index=False)
vendors_df.to_sql('vendors', conn, if_exists='replace', index=False)

#Calculating the Delay Rate
df = pd.read_sql("""
SELECT vendor_name AS vendor, location, 
    COUNT(order_id) AS total_orders, 
    COUNT(CASE WHEN order_status = 'Delayed' THEN 1 END) AS delayed_orders
FROM vendors
JOIN orders on orders.vendor_id = vendors.vendor_id
GROUP BY vendor_name, location
""", conn)

df['delay_rate'] = df['delayed_orders'] / df['total_orders']

df.to_csv('supply_chain_summary.csv', index=False)

# 4. Close your connection when done
conn.close()