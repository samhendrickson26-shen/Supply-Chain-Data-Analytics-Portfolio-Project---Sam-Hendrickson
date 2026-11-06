-- Pulling All Delayed Orders
SELECT order_date, estimated_date, actual_date, units_ordered AS units, shipping_cost AS cost, location, vendor_name AS vendor
FROM orders
JOIN vendors ON orders.vendor_id = vendors.vendor_id
WHERE order_status = 'Delayed';

-- Pulling Vendor and Location for Delayed Orders (1st draft)
SELECT vendor_name AS vendor, location, COUNT(order_id) AS delayed_orders
FROM vendors
JOIN orders on orders.vendor_id = vendors.vendor_id
WHERE order_status = 'Delayed'
GROUP BY vendor_name, location;

--Pulling Delayed Orders from Vendors and their Locations (final draft)
SELECT vendor_name AS vendor, location, 
    COUNT(order_id) AS total_orders, 
    COUNT(CASE WHEN order_status = 'Delayed' THEN 1 END) AS delayed_orders,
    ROUND(100.0 * COUNT(CASE WHEN order_status = 'Delayed' THEN 1 END) / COUNT(order_id), 1) AS delay_rate_pct
FROM vendors
JOIN orders on orders.vendor_id = vendors.vendor_id
GROUP BY vendor_name, location
ORDER BY delay_rate_pct DESC;