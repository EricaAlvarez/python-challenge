# # # PyBank # # #

# Import the os module (allows to create file paths across operating system)
import os

# Imports CVS module
import csv

# Imports currency and date formatting
import locale

# Follows the file path
budget_path = os.path.join("PyBank","Resources","budget_data.csv")

# Open and read csv
with open(budget_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    # Read the header row first
    header = next(csv_reader)

    # List creation (to hold the values from the columns later)
    Date = []
    PnL = []
    Change = []
    Monthly_change = []

    # Starting values
    greatest_increase = 0
    increase_month = ''
    greatest_decrease = 0
    decrease_month = ''

    # Foor loop trough the rows
    for row in csv_reader:

        # Adds every new value into a list
        Date.append(row[0])
        PnL.append(int(row[1]))
        Change.append(int(row[1]))
             
        # Determinates de months lists lengh
        months = len(Date)

        # Finds the biggest increase and decrease
        if int(row[1]) > greatest_increase:
            increase_month = (row[0])
            greatest_increase = int(row[1])
        elif int(row[1]) < greatest_decrease:
            decrease_month = (row[0])
            greatest_decrease = int(row[1])

    # Calculates proffit and losses total
    total = sum(PnL,3)
    
    # Follows monthly changes
    for i in range(len(Change)-1):
        change_per_month = (Change[i+1] - Change[i])
        Monthly_change.append(change_per_month)

    # Calculate average
    average_change = round(sum(Monthly_change)/len(Monthly_change),2)

# PRINTS THE FOLLOWING VALUES:
'''
    The total number of months included in the dataset
    The net total amount of "Profit/Losses" over the entire period
    The changes in "Profit/Losses" over the entire period, and then the average of those changes
    The greatest increase in profits (date and amount) over the entire period
    The greatest decrease in profits (date and amount) over the entire period
'''

print(f"""
      Financial Analysis
      ----------------------------
      Total Months: {months}
      Total: $ {total}
      Averae Change: $ {average_change}
      Greatest Increase in Profits: {increase_month} $ {greatest_increase}
      Greatest Decrease in Profits: {decrease_month} $ {greatest_decrease}
      """)

# EXPORTS RESULTS TO TEXT FILE:

f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("___________________________________")

f.write("Total Months: " + str(months))
f.write("Average Change is: $" + str(round(average_change, 2)))
f.write("Total: $" + str(total))
f.write("Greatest Increase in Profits: " + str(increase_month) + "  ($" + str(greatest_increase) + ")")
f.write("Greatest Decrease in Profits: " + str(decrease_month) + "  ($" + str(greatest_decrease) + ")")
