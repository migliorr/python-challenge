import os
import csv

#define path to get csv file
csvpath = os.path.join('resources','election_data.csv')

#Read csv file
with open(csvpath) as csvfile:
  elect_dt = csv.reader(csvfile, delimiter=',')

#Get Header
  csv_header = next(elect_dt)

#Define variables for month and totals
  total_votes= 0
  cand_vote_perc = 0
  cand_vote_num = 0
  winner = 0
  Result = {}
  res_perc = {}
  limit = 0 #aux to print winner + votes
 # final_var = {'candp': 0, 'candn': cand_vote_num, 'winner': winner}
  
#Total of casted votes

#Loop thru the file to Calc Results by candidate
  for votes in elect_dt:
      #Calc number Total of votes
    total_votes += 1
      #Cacl votes by candidate
    if votes[2] in Result:  #Already exist in dict
        Result[votes[2]] = int(Result[votes[2]])+1
    else:  #Doesn't exist yet, add to dict
        Result[votes[2]] = 1

#Loop thru Results to calculate %
for cand in sorted(Result.values(),reverse=True):
   res_perc[list(Result.keys())[list(Result.values()).index(cand)]] = str(round((cand/total_votes)*100,3))+'% ('+ str(cand) + ')'

#Print Header
print('Election Results')
print('-------------------------------')

#Print total number of votes
print ('Total Votes: ' + str(total_votes))
print('-------------------------------')

#Print Candidates, percents and votes
for cand in res_perc.values():
 print(list(res_perc.keys())[list(res_perc.values()).index(cand)], end = ':')
 print(cand)

#Print list of candidates
print('Candidates are: ')
for i in Result.keys():
    print (i, end =", ")

#Print winner and respective votes
print('')
for i in sorted(Result.values(),reverse=True):
    limit += 1
    print(f'Winner is: ', list(Result.keys())[list(Result.values()).index(i)], ' With: ', sorted(Result.values(),reverse=True)[(0)], ' Votes')
 #   print(list(Result.keys())[list(Result.values()).index(i)])
    if limit ==1:
       break
