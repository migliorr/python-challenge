import os
import csv

#define path to get csv file
csvpath = os.path.join('resources','budget_data.csv')

#Read csv file
with open(csvpath) as csvfile:
  budget_data = csv.reader(csvfile, delimiter=',')

#Get Header
  budget_header = next(budget_data)
  print(budget_header)

#Define variables for month and totals
  monthsnumber= []
  month_counter = 0
  total = 0
  avg_change = 0
  prev_budget = 0
  big_incr = ''
  month_incr = 0
  month_decr = 0

#Loop thru the file to Calc Results
  for months in budget_data:
      #Calc Budget Total    
    total += int(months[1])
      #Calc change
    if budget_data.line_num > 2:
        avg_change = avg_change + int(months[1]) - prev_budget 
          #Calc Greatest increase in profits
        if month_incr < (int(months[1]) - prev_budget):
            big_incr = months[0] + ' ' + str((int(months[1]) - prev_budget))
            month_incr = (int(months[1]) - prev_budget)
           #Calc Greatest decrease in profits
        if month_decr > (int(months[1]) - prev_budget):
            big_decr = months[0] + ' ' + str((int(months[1]) - prev_budget))
            month_decr = (int(months[1]) - prev_budget)
      #Calc Number of Monts
    if months in monthsnumber:continue
    else: monthsnumber.append(months)
      #save previous month budget for avg change
    prev_budget = int(months[1])

#Calc Avg Change
avg_change = avg_change / (len(monthsnumber)-1)

#Print Results
print ('Total Months: ' + str(len(monthsnumber)))
print (f'Total: ' ,total)
print (f'Average Change: ' , avg_change)
print (f'Greatest Increase: ' , big_incr)
print (f'Greatest Decrease: ' , big_decr)
