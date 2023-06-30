# # # PyBank # # #

# Import the os module (allows to create file paths across operating system)
import os

# Imports CVS module
import csv

# Follows the file path
budget_path = os.path.join("PyBank","Resources","budget_data.csv")


# Open and read csv
with open(budget_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Calculates the number of months
    rows_number = csv_file.readlines()
    months_number = (len(rows_number))

    # Calculates the net total amound of "Profit/Losses"
    

    # Loop through the data
    #for row in csv_reader:

      

# Prints Analysis Results header
print("Financial Analysis")
print("----------------------------")     

# PRINT THE TOTAL NUMBER OF MONTHS INCLUDED IN THE DTASET
print ("Total Months:", months_number)

# PRINT TTHE NET TOTAL AMOUNT OF "PROFIT/LOSSES" OVER THE ENTIRE PERIOD



# PRINT THE CHANGES IN "PROFIT/LOSSES" OVER THE ENTIRE PERIOD, AND THEN THE AVERAGE OF THOSE CHANGES



# PRINT THE GREATES INCREASE IN PROFITS (DATE AND AMOUND) OVER THE ENTIRE PERIOD



# PRINT THE GREATES DECREASE IN PROFITS (DATE AND AMOUND) OVER THE ENTIRE PERIOD
