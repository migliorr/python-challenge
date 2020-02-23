import os
import csv

csvpath = os.path.join('.','budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  #print(csvreader)
  csv_header = next(csvreader)
  #print(csv_header)
  month_counter = 0
  total = 0
  for row in csvreader:
      #print(row)
    month_counter = month_counter + 1
      #or col in row[1]:
       # print((col))
    total += int(row[1])
print("Total Months:" + str(month_counter))
print("Total: " + str(total))