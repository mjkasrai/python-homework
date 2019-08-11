# import libraries

from pathlib import Path
import csv

# set file path

csv_path = Path("budget_data.csv")
output_path = Path("output.txt")

# initialize variables and dictionary

pl_delta = {}
total = 0
delta = 0
total_change = 0
max = 0
min = 0
min_date = ""
max_date = ""

# read in file and create dictionary from columns

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    profit_losses = {row[0]:int(row[1]) for row in csvreader}
    
months = (len(profit_losses))

# determine delta of profit/losses and update to dictionary

for date, pl in profit_losses.items():
    pl_delta.update({date:pl-delta})
    delta = pl
    total += pl

pl_delta.pop('Jan-2010')

# determine the min and max values and sum the total

for change in pl_delta.values():
    total_change += change
    if change < min:
        min = change
    elif change > max:
        max = change

# calculate the average

avg_delta = round((total_change / len(pl_delta)),2)

# locate the date for the min and max values

for date, pl in pl_delta.items():
    if pl == min:
        min_date = date
    elif pl == max:
        max_date = date

# print to terminal

print("\n")
print("Financial Analysis\n")
print("--------------------\n")
print(f"Total Months: {months}\n")
print(f"Total: ${total}\n")
print(f"Average Change: ${avg_delta}\n")
print(f"Greatest Increase in Profits: {max_date} (${max})\n")
print(f"Greatest Decrease in Profits: {min_date} (${min})\n")

# write output to text file

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("\n")
    file.write("--------------------\n")
    file.write("\n")
    file.write(f"Total Months: {months}\n")
    file.write("\n")
    file.write(f"Total: ${total}\n")
    file.write("\n")
    file.write(f"Average Change: ${avg_delta}\n")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_date} (${max})\n")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_date} (${min})\n")