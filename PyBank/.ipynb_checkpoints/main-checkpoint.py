#PyBank Homework
# Import csv library and Path from pathlib library

import csv
from pathlib import Path

# Set filepath

budget_data_filepath = Path('C:/Users/willi/Desktop/RU-HOU-FIN-PT-07-2019-U-C/hw/02-Python/Instructions/PyBank/Resources/budget_data.csv')

# Initial empty list for budget data

budget_data =[]

# Open and read in budget data. Append rows to budget_data list

with open(budget_data_filepath,'r') as budget_file:
    csvreader =csv.reader(budget_file, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:
        budget_data.append(row)

# Initialize two empty lists for dates and profits/losses using a for loop to append
# to the lists

dates = []
profits_losses = []

for entry in budget_data:
    dates.append(entry[0])
    profits_losses.append(entry[1])
    

# Calculate total months

def count_months(dates):
    count = 0 
    for month in dates:
        count += 1
    return count

total_months = count_months(dates)

# Calculate the net total of Profit/ Losses

def net_total_profit_losses(profits_losses):
    sum = 0
    for profit_loss in profits_losses:
        sum += int(profit_loss)
    return sum

total_profit_losses = net_total_profit_losses(profits_losses)

# Define a function summary_of_changes_in_profits

def summary_of_changes_in_profits(profits_losses):
    # This function will accept a list of profits/losses
    # and return a list of the monthly changes in the profits/losses
    
    index = 0
    monthly_changes = []
    change = 0
    previous_month_profit_loss = 0
    
    # Use a for loop to make a list of changes in monthly profit/loss
    
    for monthly_profit_loss in profits_losses :
        if previous_month_profit_loss == 0:
            previous_month_profit_loss = monthly_profit_loss
        else:
            change = int(monthly_profit_loss) - int(previous_month_profit_loss)
            monthly_changes.append(change)
            previous_month_profit_loss = monthly_profit_loss
    return monthly_changes

# Initialize empty list and call summary_of_changes_in_profits to get list of changes

summary_of_changes = []
summary_of_changes = summary_of_changes_in_profits(profits_losses)


# Define function avg_change 
    
def avg_change(summary_of_changes):
    # This function will take in the list of summary_of changes and return
    # the average change
    
    count = 0
    sum = 0
    mean_change = 0
    for change in summary_of_changes:
        sum += change
        count += 1
    mean_change = sum/count    
    return mean_change

# Call avg_change function providing summary_of_changes list

average_change = round(avg_change(summary_of_changes), 2)

        
# Find the max increase and min increase in monthly profits 

max_increase = 0
min_increase = 0
count = 0
for change in summary_of_changes:
    if max_increase == 0 and min_increase == 0:
        max_increase = change
        min_increase = change
    elif change > max_increase:
        max_increase = change
    elif change < min_increase:
        min_increase = change
        

# Find the date of the max_increase and the date of the min_increase

index_of_date_of_max_increase = (summary_of_changes.index(max_increase) + 1)
index_of_date_of_min_increase = (summary_of_changes.index(min_increase) + 1)
date_of_max_increase = dates[index_of_date_of_max_increase]
date_of_min_increase = dates[index_of_date_of_min_increase]


# Print analysis to terminal 

print(f"Financial Analysis")
print(f"------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_of_max_increase} (${max_increase})")
print(f"Greatest Decrease in Profits: {date_of_min_increase} (${min_increase})")

# Export analysis to a text file

output_path = 'output.txt'

with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {date_of_max_increase} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {date_of_min_increase} (${min_increase})\n")
