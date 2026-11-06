# Supply Chain/Data Analysis Synthetic Dataset Project - Sam Hendrickson

### Key Findings:
Delay Rates and Total Orders for Each Vendor:

Adam's Collection: 74.1%, 27 Total Orders

Bob's B-21's: 85%, 20 Total Orders

John's Products: 63.6%, 22 Total Orders

Sam's Storage: 73.7%, 19 Total Orders

Tim's Inc: 83.3%, 12 Total Orders (sample size this small is not reliable to analyze delay rates)


### Project Context:

In this project, I am a Supply Chain Analyst at Boeing, based in Kankakee, Illinois (This is a fictional Boeing site and scenario with fully synthetic data; no real Boeing data was used). I am pulling a dataset full of vendor order information, and I am trying to find the vendors that have the highest amount of “delayed” order rates. The parameters of a delayed order were set in my Python code, and they are as follows: Estimated Delivery Days: 7 to 14 days. I created an “Actual Delivery Days” to create some randomization when it came to the delivery’s arrival times, and I made that range 7 to 21 days, here were the results. 

![Tableau Supply Data](Boeing%20Vendor%20Delay%20Rate%20Table.PNG)

### Coding Methodology:

(Disclaimer: I used Gemini as a Teacher and a guide to help me with unknown syntax and libraries)

I used Python to create the supply chain database (supply_chain.db) that my SQL queries would eventually collect and sort data from. Since I didn’t really know of any online .db files I could pull from, I decided that I wanted to create as realistic of an order database as I could. You can see how I constructed my databases in my ‘supply_chain.sql’ tab in GitHub, but the main columns that I made Python create and randomize data for were order_id (total_orders), order_status, estimated_date, and actual_date. I learned a few tricks on how the ‘Random’ library works when creating data for a .db, and I really wanted to carefully create this portion of my code, so that the data that was created would be as realistic as possible. For my SQL queries, I wanted to create a basic query that would pull all Delayed Orders, and then from there, I wanted to refine that query, until I got each vendor, their location, their total orders, and total delayed orders. I made vendor_id the foreign key in my ‘orders’ table, and my primary key in my vendors table. And to pull the count of total orders and delayed orders, I simply used the COUNT aggregate to tally the total orders (used order_id), and used a CASE statement to separate the ‘delayed’ orders from the total, using “order_status = ‘Delayed’”. The delay rate was not something I added inside my SQL tables or queries, but instead was added in my Python code. I had to create a CSV file for Tableau (couldn’t read .db’s unfortunately), and it helped create a bar graph for comparing delay rates between vendors.

### Analytical Assumption and Interpretation 

I ran into a problem: I created the code to create random data for total units ordered, shipping costs, location of vendors, and stopped to consider: Wouldn’t delayed orders have a higher correlation to those 3 factors if the amount of units shipped were higher, shipping costs were higher, and the distance from the vendor to my company (Boeing) was further away than the others were? I almost went into the code to create probability factors that would give higher units in an order a higher chance of being ‘delayed’ for example, but I am glad I didn’t. Because the data isn’t what makes these orders delayed, it’s what happens at the vendor sites, the supply and demand of the companies needed parts, and a multitude of other factors that father those symptoms (symptoms that I thought were the delta of the delayed orders). That’s when I realized having these numbers being totally randomized is what makes this such a realistic scenario for any kind of Data/Supply/Business Analyst: you have to interpret what those numbers are saying, and not make assumptions when you don’t have the full picture. And if this was a real scenario at a Boeing site in Kankakee, IL, I wouldn't have the full picture. I don’t have that enterprise, C-Suite information to know why Bob’s B-21's out of Indianapolis had the highest Delay Rate out of the 5 vendors, but I can make a hypothesis for these symptoms. Bob's B-21's and Tim’s Inc share the highest Delay Rate:  Bob’s procurement process could be the worst of the group. They could always be having equipment issues, and seem to never have the right materials to even fully create the parts that need to be shipped to Boeing. And Tim’s Inc honestly could have gotten the short end of the stick. They are the smallest vendor out of the 5, but they got 12 orders this month, maybe they got 5 more orders than normal, so the amount of drivers and trucks could not keep up with the orders that came in, and that also affected their assembly line work: during peak hours of order creation and fulfillment, the line may not have been ready to handle that high influx of orders, leading to delays. What I'd do if these were the potential limiting factors on these vendors? For Bob's, I would research the part type that is hindering their procurement process. For Tim's, I would look into their carrier information, see who's shipping their parts to our Boeing site. And I'd also look at their order volume history: I hypothesized they usually receive fewer orders than other vendors. Is that actually the case? Could that be a reason why it was so hard for them to ship to us on time? All of those factors are things that need to be looked into in order to create a fuller story for the delay rates that occurred. 

Disclaimer: the other vendors all have high delay rates because this is a synthetic dataset that was randomized, the differences in delay rates are too small to treat as meaningful since the order range per vendor is 12-27 in this case study, but for simplicity's sake, the two highest are illustrative examples. 

### Delay Rate and Map Visualizations

I uploaded the CSV with my order data into Tableau to create two simple visualizations: a bar graph, and a geographical map: 
![Vendor Map](Boeing%20Vendor%20Map.PNG)

It’s not the prettiest thing, but it allows me to compare the vendor delay rate and their respective location to our Boeing site in Kankakee. 

### Conclusion

When analyzing either supply chain data, or sales conversion data, the job of the analyst is to clean, aggregate, sort, and interpret that data to their leaders to help improve business decision making. Hopefully with further investigation into why Bob’s B-21's and Tim’s Inc have their problems, Boeing Corporate can address any procurement or capacity issues the investigation confirms, and potentially help their business run more efficiently. 

