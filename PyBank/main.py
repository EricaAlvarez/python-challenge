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
    csv_header = next(csv_file)

    # Calculates the number of months
    
    for row in csv_reader:

        Date = []
        PnL = []

        Date = (row[0])
        PnL = (row[1])

        total = sum(int(PnL))
      
        print (PnL)









# PRINTS THE FOLLOWING VALUES:
'''
    The total number of months included in the dataset
    The net total amount of "Profit/Losses" over the entire period
    The changes in "Profit/Losses" over the entire period, and then the average of those changes
    The greatest increase in profits (date and amount) over the entire period
    The greatest decrease in profits (date and amount) over the entire period
'''
