# -*- coding: UTF-8 -*-
""" Python Homework  PyBank
    Python Script that will input monthly revenue data formated in a csv
    file containing "Date", "Revenue". Output to screen and file lists 
    total number of months, total revenue, average change month over month, and
    the month and amount for the greatest increase and greatest decrease.
    
     David W. Jones           """


# Dependencies
import os
import csv

# request file names for input and output, declair the subfolder for holding the input data
# If i had time I would add an IF statement to prompt again if file not found

input_file = input(" Please enter the name of the data file (with csv ext): ")
csvpath = os.path.join("raw_data", input_file)
output_file = input("Please enter the name of the Text file to hold the Financial Review (with txt ext): ")


# Declaration of variables that will be utilized during the looping and output process

month_count=0
total_revenue=0
lrg_loss=0
loss_date="unknown"
gain_date="unknown"
lrg_gain=0
avg_delta = 0
temp=0
current_month_rev=0
prior_month_rev=0
delta=0

#looping process to gather the output information that fills the variables 
#skips the first month for calculating the monthly change (exclude) keeps a 
#running tab of months and revenue.  

with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)
    for row in reader:
        prior_month_rev=current_month_rev 
        if prior_month_rev==0:
            exclude=int(row["Revenue"])
        total_revenue=total_revenue+ int(row["Revenue"])
        month_count = month_count + 1
        # calculates the change in current month revenue and keeps total     
        current_month_rev=int(row["Revenue"])
        delta=current_month_rev-prior_month_rev
        avg_delta=avg_delta+delta
        # flags the largest loss or largest gain
        if delta > lrg_gain:
            lrg_gain=delta
            gain_date=row["Date"]
        elif delta < lrg_loss:
            lrg_loss=delta
            loss_date=row["Date"]
        
#calculates the average change over the period
avg_delta=avg_delta-exclude
delta_percentage=avg_delta/(month_count-1)
#outputs the results
print("  ")
print("--------------------------------------------------------------------")
print(" Financial Analysis")
print("--------------------------------------------------------------------")
print("Total number of months in period: " + str(month_count))
print("Total Revenue in period: $ " + str(total_revenue))
print("Average monthly change in Revenue : $" + str(delta_percentage))
print("Greatest monthly increase in Revenue : " + str(gain_date) + "   $ " + str(lrg_gain))
print("Largest monthly decrease in Revenue : " + str(loss_date) + "   $ " + str(lrg_loss))
print("--------------------------------------------------------------------")
