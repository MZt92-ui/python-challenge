
import os
import csv
from unittest import result

from bs4 import ResultSet

csv_path = os.path.join("Resources","budget_data.csv")

# read each info into a list for further analysis
month_list = []
amount_list = []
chg_list = []

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    #print(f"header is :{header}")

    for row in csv_reader:
        month_list.append(row[0])
        amount_list.append(int(row[1]))
    
    #call list methods to get summary
    period = len(month_list)
    net_total_amount = sum(amount_list)

#loop through amount list to get chg value
for i in range(len(amount_list)-1):
    chg_list.append(amount_list[i+1] - amount_list[i])
    average_chg = round(sum(chg_list) / (len(chg_list)),2)

#call list method to get specific value
greatest_inc = max(amount_list)
greatest_inc_date = month_list[amount_list.index(greatest_inc)]
greatest_dec = min(amount_list)
greatest_dec_date = month_list[amount_list.index(greatest_dec)]

#print the results
print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {period}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_chg}")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})")
print(f"Greatest decrease in Profits: {greatest_dec_date} (${greatest_dec})")

#write to txt file
Result = ["Financial Analysis\n",
        "----------------------------\n",
        f"Total Months: {period}\n",
        f"Total: ${net_total_amount}\n",
        f"Average Change: ${average_chg}\n",
        f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n",
        f"Greatest decrease in Profits: {greatest_dec_date} (${greatest_dec})\n"]
result_path = "C:/Users/Eva/Documents/GitHub/python-challenge/PyBank/analysis/result.txt"
with open(result_path,"w") as result:
    result.writelines(Result)
    result.close()