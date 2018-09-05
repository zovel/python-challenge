#get em ready
import os
import csv
budget_data=os.path.join('budget_data.csv')
net=0

#The total number of months included in the dataset
with open(budget_data,newline="") as totalmonths_csv:
    totalmonths_reader=csv.reader(totalmonths_csv,delimiter=",")
    next(totalmonths_reader,None)
    value=len(list(totalmonths_reader))

#The total net amount of "Profit/Losses" over the entire period
with open (budget_data,newline="") as profitloss_csv:
    profitloss_reader=csv.reader(profitloss_csv,delimiter=",")
    next(profitloss_reader,None)
    for row in profitloss_reader:
        net +=int(row[1])

#The average change in "Profit/Losses" between months over the entire period
with open (budget_data,newline="") as averagechange_csv:
    averagechange_reader=csv.reader(averagechange_csv,delimiter=",")
    next(averagechange_reader,None)
        #(month 2-month 1)/total count(month 1 to 86)-1//enumerate???
        #probably going to be a data function that can be input in the following two calculations

#The greatest increase in profits (date and amount) over the entire period
with open (budget_data,newline="") as greatestincrease_csv:
    greatestincrease_reader=csv.reader(greatestincrease_csv,delimiter=",")
    next(greatestincrease_reader,None)
    #use enumerate function here

#The greatest decrease in losses (date and amount) over the entire period
with open (budget_data,newline="") as greatestdecrease_csv:
    greatestdecrease_reader=csv.reader(greatestdecrease_csv,delimiter=",")
    next(greatestdecrease_reader,None)
    #use enumerate function here


#PRINT EM UP
print("Financial Analysis")
print("------------------")
print(f"Total Months: {value}")
print(f"Total: $ {net}")
#print(f"Average Change:)
#print("Greatest Increase in Profits")
#print("Greatest Decrease in Profits")
