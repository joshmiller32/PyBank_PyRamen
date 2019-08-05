# Pybank Homework Assignment

# Import budget_data.csv file by using pandas read_csv function and assign to variable budget_data 

import pandas as pd
budget_data = pd.read_csv(r"C:\Users\willi\Desktop\RU-HOU-FIN-PT-07-2019-U-C\hw\02-Python\Instructions\PyBank\Resources\budget_data.csv")

# Calculate total months included in the dataset

total_months = budget_data['Date'].count()

# Calculate the net total of Profit/Losses over entire period

net_total_of_Profit_Losses= sum(budget_data['Profit/Losses'])

# Calculate the average of the changes in Profit/Losses over entire period


def avg_of_monthly_changes(df):
    # This function will accept a dataframe with a Profit/Losses column 
    # convert the column to a list , then sum the changes in profit/loss 
    # from month to month, finally calculating the average of the changes 
    # rounded to the hundreths place
    number_of_changes = 0
    profit_losses = list(df['Profit/Losses'])
    previous_month_profit_loss = 0
    total_changes_in_profit_loss = 0
    for monthly_profit_loss in profit_losses :
        if monthly_profit_loss == profit_losses[0]:
            previous_month_profit_loss = monthly_profit_loss
            continue
        else:
            change = monthly_profit_loss - previous_month_profit_loss
            total_changes_in_profit_loss += change
            previous_month_profit_loss = monthly_profit_loss 
            number_of_changes += 1
    avg_change = round((total_changes_in_profit_loss/ number_of_changes) , 2)
    return avg_change
    

# Call avg_of_monthly_changes function providing budget_data df to calculate average change
average_change = (avg_of_monthly_changes(budget_data))


# Find the greatest increase in profits (date and amount) over the entire period
def Max_increase_Max_decrease_in_profits(df):
    # This function will accept a dataframe with the column Profit/Losses
    # and will find the greatest increase in profits with corresponding date
    # as well as the greatest decrease in profits with corresponding date
    
    
    #Initialize variables , convert Profit/Losses column to a list
    profit_losses = list(df['Profit/Losses'])
    index = 0
    summary_of_changes = []
    change = 0
    
    # Use a for loop to make a list of changes in monthly profit/loss
    for monthly_profit_loss in profit_losses :
        if monthly_profit_loss == profit_losses[0]:
            previous_month_profit_loss = monthly_profit_loss
        else:
            change = monthly_profit_loss - previous_month_profit_loss
            summary_of_changes.append(change)
            previous_month_profit_loss = monthly_profit_loss
    
    # Find the maximum increase in profits
    max_increase = max(summary_of_changes)        
    
    # Find the index of the Date of maximum increase in profits
    index_of_max_increase = (summary_of_changes.index(max_increase)) + 1
    
    # Find date of the maximum increase in profits
    date_of_max_increase = df.iloc[index_of_max_increase ,0]
    
    # Find the maximum decrease in profits 
    max_decrease = min(summary_of_changes)
    
    # Find the index of the Date of the maximum decrease in profits
    index_of_max_decrease = (summary_of_changes.index(max_decrease)) + 1
    
    # Find the date of the maximum decrease in profits
    date_of_max_decrease = df.iloc[index_of_max_decrease, 0]
    
    # Return a tuple with values for max_increase, date_of_max_increase, max_decrease, date_of_max_decrease
    return (max_increase, date_of_max_increase, max_decrease, date_of_max_decrease)

# Call function to calculate max_incrase, date_of_max_increase, max_decrease, date_of_max_decrease
max_changes_and_dates = Max_increase_Max_decrease_in_profits(budget_data)   

# Unpack tuple and assign to variables greqtest_increase, date_of_greatest_increase, greatest_decrease, date_of_greatest_increase 
greatest_increase, date_of_greatest_increase, greatest_decrease, date_of_greatest_decrease = max_changes_and_dates

# Print analysis to terminal 
print(f"Financial Analysis")
print(f"------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_of_Profit_Losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})")

# Export analysis to a text file
output_path = 'output.txt'

with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total_of_Profit_Losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})\n")


