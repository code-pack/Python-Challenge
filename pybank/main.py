
import os
import csv

# request file names for input and output, declair the subfolder for holding the data
# If i had time I would add an IF statement to prompt again if file not found

input_file = input(" Please enter the name of the data file (with csv ext): ")
csvpath = os.path.join("raw_data", input_file)
output_file = input("Please enter the name of the Text file to hold the Financial Review (with txt ext): ")


# Read the csv and convert it into a list of dictionaries

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




with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)
    for row in reader:
        prior_month_rev=current_month_rev 
        if prior_month_rev==0:
            exclude=int(row["Revenue"])
            exclude_date=row["Date"]
        total_revenue=total_revenue+ int(row["Revenue"])
        month_count = month_count + 1
        
        current_month_rev=int(row["Revenue"])
        delta=current_month_rev-prior_month_rev
        avg_delta=avg_delta+delta
        if delta > lrg_gain:
            lrg_gain=delta
            gain_date=row["Date"]
        elif delta < lrg_loss:
            lrg_loss=delta
            loss_date=row["Date"]
        

avg_delta=avg_delta-exclude
delta_percentage=avg_delta/(month_count-1)


print(total_revenue)
print(month_count)
print(lrg_gain)
print(lrg_loss)
print(loss_date)
print(gain_date)
print(avg_delta)
print(delta_percentage)
print(exclude)
print(exclude_date)




#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)   
