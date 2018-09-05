#get em ready
import os
import csv
budget_data=os.path.join('budget_data.csv')
net=0
total=0

#The total number of months included in the dataset
with open(budget_data,newline="") as totalmonths_csv:
    totalmonths_reader=csv.reader(totalmonths_csv,delimiter=",")
    next(totalmonths_reader,None)
    for row in totalmonths_reader:
        total+=int(row[0])
        
#The total net amount of "Profit/Losses" over the entire period
with open (budget_data,newline="") as profitloss_csv:
    profitloss_reader=csv.reader(profitloss_csv,delimiter=",")
    next(profitloss_reader,None)
    for row in profitloss_reader:
        net +=int(row[1])

#The average change in "Profit/Losses" between months over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#PRINT EM UP
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total}")
print(f"Total: $ {net}")
