CREATE TABLE vendors 
vendor_id INTEGER PRIMARY KEY,
vendor_name TEXT,
location_region TEXT

CREATE TABLE orders
order_id INTEGER PRIMARY KEY,
vendor_id INTEGER FOREIGN KEY,
order_date DATE,
estimated_date DATE,
actual_date DATE,
order_status TEXT,
units_ordered INTEGER,
shipping_cost DECIMAL