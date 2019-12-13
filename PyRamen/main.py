# PyRamen 
# Import csv and Path
import csv
from pathlib import Path

# Create file_paths for menu and sales data
menu_filepath = Path('../Desktop/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyRamen/Resources/menu_data.csv')
sales_filepath = Path('../Desktop/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyRamen/Resources/sales_data.csv')

# Initialize empty lists for menu and sales data

menu = []
sales = []

# Append rows to menu list

with open(menu_filepath,'r') as menu_file:
    csvreader1 = csv.reader(menu_file, delimiter = ',')
    header = next(csvreader1)
    for row in csvreader1 : 
        menu.append(row)

#Append rows to sales list

with open(sales_filepath,'r') as sales_file:
    csvreader2 = csv.reader(sales_file, delimiter = ',')
    header = next(csvreader2)
    for row in csvreader2 :
        sales.append(row)      

# Initialize empty dict and quantity variable 

report = {}
quantity = 0

# Create report in first loop over sales list, then update report in nested loop
# with the values for count,revenue,cogs, and profit 

for record in sales :
    quantity += int(record[3])
    sales_item = record[4]     
    report[sales_item] = { "01-count": 0, "02-revenue": 0,"03-cogs": 0,"04-profit": 0}
    for record in menu :
        item = record[0]
        price = float(record[3])
        cost = int(record[4])
        if sales_item == item:
            profit = price - cost 
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else :
            #print(f"{sales_item} does not equal {item}! NO MATCH!")
            continue
            

# Write contents of report to text file

output_path = 'PyRamen_report.txt'

with open(output_path, 'w') as file:
    file.write(f"{report}")

