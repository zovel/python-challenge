import os
import csv
net=0
profit_loss=[]
total_months=0
greatest_increase, greatest_decrease=0,0
difference=0
month_1=""
month_2=""
budget_data=os.path.join("budget_data.csv")
with open(budget_data,newline="") as budget_csv:
    budget_reader=csv.reader(budget_csv,delimiter=",")
    next(budget_reader,None)
    total_months +=1
    first_row= next(budget_reader)
    change=int(first_row[1])
    net=int(first_row[1])
    def change_in_profit_loss(change):
        return((int(row[1]))-change)
    for row in budget_reader:
        total_months +=1
        net += int(row[1])
        difference= change_in_profit_loss(change)
        change=int(row[1])
        profit_loss.append(difference)
        if difference >= greatest_increase:
            greatest_increase= difference
            month_1= (row[0])
        elif difference <= greatest_decrease:
            greatest_decrease= difference
            month_2=(row[0])
    average_change= (sum(profit_loss)/int(len(profit_loss)))

#PRINT EM UP
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: $ {net}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase: {month_1} $ {greatest_increase}")
print(f"Greatest Decrease: {month_2} $ {greatest_decrease}")