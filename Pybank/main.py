import os

import csv

dates = []
monthly_totals = []
total_months = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
overall_change = 0


csvpath = os.path.join('..','Resources', 'budget_data.csv')

#open the file and create seperate lists from the information
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

#create lists to hold the dates and profits and losses
    for row in csvreader:
        dates.append(row[0])
        monthly_totals.append(row[1])

#find the total number of months
    for i in dates:
        total_months += 1

    #find the net total of every number
    for i in monthly_totals:
        net_total += int(i)

    start_total = int(monthly_totals[0])
    end_total = int(monthly_totals[-1])

    monthly_changes_list = []
    month_1 = int(monthly_totals[0])
    month_2 = 0
    monthly_change = 0
    greatest_increase_date = ""

#create a monthly change list
    for i in monthly_totals:
        month_2 = int(i)
        monthly_change = month_2 - month_1
        month_1 = month_2
        monthly_changes_list.append(monthly_change)

#find the overall change
    overall_change = end_total - start_total

#find the average change
    average_change = round(overall_change/(total_months - 1), 2)
    
#find the greatest increase and decrease amounts
    greatest_increase = max(monthly_changes_list)
    greatest_decrease = min(monthly_changes_list)
    greatest_decrease_date = ""

#find the greatest increase and decrease dates
    for i in range(1, len(monthly_changes_list)):
        if monthly_changes_list[i] == greatest_increase:
            greatest_increase_date = dates[i]
        elif monthly_changes_list[i] == greatest_decrease:
            greatest_decrease_date = dates[i]
        
#print the results
print("Financial Analysis")
print("-----------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


#export the results
output_result = os.path.join("..", "Analysis", "results.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("----------------- \n"),
    txt_file.write(f"Total Months: {total_months} \n"),
    txt_file.write(f"Total: ${net_total} \n"),
    txt_file.write(f"Average Change: ${average_change}\n"),
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"),
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
        

    
    

            
            


